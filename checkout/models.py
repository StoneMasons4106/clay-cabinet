import random
import string

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from products.models import Product
from profiles.models import UserProfile

from decimal import Decimal


class OrderProgress(models.Model):

    class Meta:
        verbose_name_plural = 'OrderProgress'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.friendly_name

    def get_name(self):
        return self.name


class Order(models.Model):
    order_number = models.CharField(max_length=10, null=False, editable=False)
    order_progress = models.ForeignKey('OrderProgress', null=True, blank=True, on_delete=models.SET_NULL)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    sales_tax = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')
    custom_order_notes = models.TextField(max_length=1024, null=True, blank=True)
    courier = models.CharField(max_length=50, null=True, blank=True)
    tracking_number = models.CharField(max_length=80, null=True, blank=True)
    discount_code = models.CharField(max_length=50, null=True, blank=True)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        output_string = ''.join(random.SystemRandom().choice(string.ascii_letters.upper() + string.digits) for _ in range(10))
        return output_string

    def check_discount_code(self):
        discount_codes = DiscountCode.objects.values()
        count = 0
        for discount_code in discount_codes:
            if self.discount_code == discount_code["code"]:
                response = {
                    'discount': 'True', 
                    'percent_off': str(discount_code["percent_off"]),
                }
                return response
            else:
                count = count + 1
                if count == len(discount_codes):
                    response = {
                        'discount': 'False',
                    }
                    return response
                continue

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        self.sales_tax = self.order_total * Decimal(settings.SALES_TAX_PERCENTAGE / 100)
        grand_total = Decimal(self.order_total) + Decimal(self.delivery_cost) + Decimal(self.sales_tax)
        if self.discount_code:
            discount_code_response = self.check_discount_code()
            if discount_code_response["discount"] == 'False':
                self.grand_total = grand_total
            else:
                self.grand_total = round(grand_total * Decimal((1 - (int(discount_code_response["percent_off"]) / 100))), 2)
        else:
            self.grand_total = grand_total
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'


class DiscountCode(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    code= models.CharField(max_length=50, null=False, blank=False)
    percent_off = models.DecimalField(max_digits=2, decimal_places=0, null=False, default=0)

    def __str__(self):
        return self.name