from django.contrib import admin
from .models import Order, OrderLineItem, OrderProgress


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'sales_tax', 'order_total',
                       'grand_total', 'original_cart',
                       'stripe_pid')

    fields = ('order_number', 'date', 'order_progress', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'sales_tax', 'order_total', 'grand_total',
              'original_cart', 'stripe_pid', 'custom_order_notes', 'courier', 
              'tracking_number')

    list_display = ('order_number', 'date', 'order_progress', 'full_name',
                    'order_total', 'delivery_cost',
                    'sales_tax', 'grand_total',)

    ordering = ('-date',)


class OrderProgressAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProgress, OrderProgressAdmin)
