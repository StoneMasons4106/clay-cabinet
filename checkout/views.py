from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.template.loader import render_to_string
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from cart.models import UserCart
from hubspot_api_calls import create_new_contact, create_new_deal
from .forms import OrderForm
from .models import Order, OrderLineItem, OrderProgress
from products.models import Product
from cart.contexts import cart_contents
from profiles.models import UserProfile
import stripe
import json


def cache_checkout_data(request):
    if request.method == 'POST':
        try:
            try:
                cart = get_object_or_404(UserCart, user=request.user)
                jsonready_cart = cart.cart.replace("'", '"')
                user_cart = json.loads(jsonready_cart)
            except:
                user_cart = request.session.get('cart', {})
            pid = request.POST.get('client_secret').split('_secret')[0]
            stripe.api_key = settings.STRIPE_SECRET_KEY
            stripe.PaymentIntent.modify(pid, metadata={
                'cart': json.dumps(user_cart),
                'save_info': request.POST.get('save_info'),
                'username': request.user,
            })
            return HttpResponse(status=200)
        except Exception as e:
            messages.error(request, 'Sorry, your payment cannot be \
                processed right now. Please try again later.')
            return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        try:
            user_cart = get_object_or_404(UserCart, user=request.user)
            jsonready_cart = user_cart.cart.replace("'", '"')
            cart = json.loads(jsonready_cart)
        except:
            cart = request.session.get('cart', {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
            'custom_order_notes': request.POST['custom_order_notes'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            if request.user.username:
                order.user_profile = get_object_or_404(UserProfile, user=request.user)
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.order_progress = get_object_or_404(OrderProgress, name='open')
            current_cart = cart_contents(request)
            order.order_total = float(current_cart["total"])
            order.delivery_cost = order.order_total * (settings.STANDARD_DELIVERY_PERCENTAGE / 100)
            order.sales_tax = order.order_total * (settings.SALES_TAX_PERCENTAGE / 100)
            order.grand_total = order.order_total + order.delivery_cost + order.sales_tax
            order.save()
            for item_id, item_data in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for quantity in item_data.items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                            )
                            order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your cart wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))

            request.session['save_info'] = 'save-info' in request.POST
            first_name = order.full_name.split(' ')[0]
            last_name = order.full_name.split(' ')[1]
            contact_id = create_new_contact(order.email, first_name, last_name)
            create_new_deal(contact_id, order.grand_total)
            send_order_confirmation(request, order)

            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            pass
    else:
        try:
            cart = get_object_or_404(UserCart, user=request.user)
        except:
            cart = request.session.get('cart', {})
        if not cart:
            return redirect(reverse('products'))

        current_cart = cart_contents(request)
        count = 0
        for item in current_cart["cart_items"]:
            count += item["quantity"]
        total = float(current_cart["total"])
        delivery_cost = total * (settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        sales_tax = total * (settings.SALES_TAX_PERCENTAGE / 100)
        grand_total = total + delivery_cost + sales_tax
        stripe_total = round(grand_total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

    template = 'checkout/checkout.html'
    
    context = {
        'page': 'checkout',
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'categories': current_cart["categories"],
        'cart_items': current_cart["cart_items"],
        'total': total,
        'delivery': delivery_cost,
        'sales_tax': sales_tax,
        'grand_total': grand_total,
        'product_count': count,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.username:
        cart = get_object_or_404(UserCart, user=request.user)
        cart.delete()
        try:
            del request.session['cart']
        except:
            pass
    else:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'page': 'checkout_success',
        'order': order,
    }

    return render(request, template, context)


def send_order_confirmation(request, order):

    if request.method == 'POST':
        
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone_number')
        address = request.POST.get('street_address1')
        town_or_city = request.POST.get('town_or_city')
        county = request.POST.get('county')
        country = request.POST.get('country')
        zipcode = request.POST.get('postcode')
        order_number = order.order_number
        date = order.date
        order_total = order.order_total
        delivery_cost = order.delivery_cost
        sales_tax = order.sales_tax
        grand_total = order.grand_total

        confirmation_message = render_to_string(
            'checkout/emails/order_confirmation.txt', {
                'full_name': full_name,
                'email': email,
                'phone': phone,
                'address': address,
                'town_or_city': town_or_city,
                'county': county,
                'country': country,
                'zipcode': zipcode,
                'order_number': order_number,
                'order_date': date,
                'order_total': round(order_total, 2),
                'delivery_cost': round(delivery_cost, 2),
                'sales_tax': round(sales_tax, 2),
                'grand_total': round(grand_total, 2),
                'order': order,
            }
        )

        notification_message = render_to_string(
            'checkout/emails/order_notification.txt', {
                'full_name': full_name,
                'email': email,
                'phone': phone,
                'address': address,
                'town_or_city': town_or_city,
                'county': county,
                'country': country,
                'zipcode': zipcode,
                'order_number': order_number,
                'order_date': date,
                'order_total': round(order_total, 2),
                'delivery_cost': round(delivery_cost, 2),
                'sales_tax': round(sales_tax, 2),
                'grand_total': round(grand_total, 2),
                'order': order,
            }
        )

        confirmation_message_wrapper = EmailMessage(
            '[ClayCabinet] Thank you for your order!',
            confirmation_message,
            to=[email]
        )

        notification_message_wrapper = EmailMessage(
            f'New Order Number: {order_number}',
            notification_message,
            to=[settings.DEFAULT_FROM_EMAIL]
        )

        confirmation_message_wrapper.send()
        notification_message_wrapper.send()
