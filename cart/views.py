from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from . import contexts
from .models import UserCart
from django.contrib import messages
import json

from products.models import Product

# Create your views here.

def view_cart(request):
    """ A view that renders the cart contents page """

    context = contexts.cart_contents(request)
    template = 'cart/cart.html'
    return render(request, template, context)


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """
        
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    
    if request.user.username:
        
        try:
            cart = get_object_or_404(UserCart, user=request.user)
            jsonready_cart = cart.cart.replace("'", '"')
            user_cart = json.loads(jsonready_cart)

            if item_id in user_cart.keys():
                user_cart[item_id] += quantity
                cart.cart = user_cart
                cart.save()
                messages.success(request, f'Updated {product.name} quantity to {quantity}')
            else:
                user_cart[item_id] = quantity
                cart.cart = user_cart
                cart.save()
                messages.success(request, f'Added {quantity} {product.name} to your cart')
        
        except:
            user_cart = {}

            user_cart[item_id] = quantity
            cart = UserCart(user=request.user)
            cart.cart = user_cart
            cart.save()
            messages.success(request, f'Added {quantity} {product.name} to your cart')

        request.session['cart'] = cart.cart
    
    else:
        
        cart = request.session.get('cart', {})
        
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {quantity}')
        else:
            cart[item_id] = quantity
            messages.success(request, f'Added {quantity} {product.name} to your cart')
        
        request.session['cart'] = cart
    
    return redirect(redirect_url)
    

def adjust_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    
    if request.user.username:
        
        cart = get_object_or_404(UserCart, user=request.user)
        
        if quantity > 0:
            jsonready_cart = cart.cart.replace("'", '"')
            json_cart = json.loads(jsonready_cart)
            json_cart[item_id] = quantity
            cart.cart = json_cart
            cart.save()
            messages.success(request, f'Updated {product.name} quantity to {quantity}')
        else:
            json_cart = cart.cart.replace("'", '"')
            json.loads(json_cart).pop(item_id)
            cart.cart = json_cart
            cart.save()
            messages.success(request, f'Removed {product.name} from your cart')
        request.session['cart'] = json_cart

    else:

        cart = request.session.get('cart', {})

        if quantity > 0:
                cart[item_id] = quantity
                messages.success(request, f'Updated {product.name} quantity to {cart[item_id]}')
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {product.name} from your cart')

        request.session['cart'] = cart
    
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""

    if request.method == 'POST':

        if request.user.username:
        
            try:
                product = get_object_or_404(Product, pk=item_id)
                cart = get_object_or_404(UserCart, user=request.user)

                jsonready_cart = cart.cart.replace("'", '"')
                json_cart = json.loads(jsonready_cart)
                json_cart.pop(item_id)
                cart.cart = json_cart
                cart.save()
                messages.success(request, f'Removed {product.name} from your cart')

                request.session['cart'] = json_cart
                return HttpResponse(status=200)

            except Exception as e:
                return HttpResponse(status=500)

        else:

            try:
                product = get_object_or_404(Product, pk=item_id)
                cart = request.session.get('cart', {})

                cart.pop(item_id)
                messages.success(request, f'Removed {product.name} from your cart')

                request.session['cart'] = cart
                return HttpResponse(status=200)

            except Exception as e:
                return HttpResponse(status=500)
