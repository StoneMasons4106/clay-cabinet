from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from .models import OrderLineItem, Order


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.update_total()

@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.update_total()

@receiver(post_save, sender=Order)
def update_order_on_save(sender, instance, created, **kwargs):
    """
    Send shipped email if order is shipped, has a courier and tracking number exists
    """
    if created:
        pass
    else:
        try:
            if instance.order_progress.friendly_name == 'Shipped' and instance.courier != None and instance.tracking_number != None:
                if instance.grand_total == 0:
                    '''When orders are deleted, the total is 0. 
                    This prevents emails going out if an order is deleted.'''
                    pass
                else:
                    shipped_message = render_to_string(
                        'checkout/emails/order_shipped.txt', {
                            'order_number': instance.order_number,
                            'order_date': instance.date,
                            'order_total': round(instance.order_total, 2),
                            'delivery_cost': round(instance.delivery_cost, 2),
                            'sales_tax': round(instance.sales_tax, 2),
                            'grand_total': round(instance.grand_total, 2),
                            'order': instance,
                            'courier': instance.courier,
                            'tracking_number': instance.tracking_number
                        }
                    )

                    shipped_message_wrapper = EmailMessage(
                        f'[ClayCabinet] Your Order Has Shipped!',
                        shipped_message,
                        to=[instance.email]
                    )

                    shipped_message_wrapper.send()
        except:
            pass