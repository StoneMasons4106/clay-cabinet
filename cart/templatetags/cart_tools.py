from django import template
from cart.contexts import cart_contents

register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity


@register.simple_tag(name='cart_grand_total')
def cart_grand_total(request):
    context = cart_contents(request)
    total = context["grand_total"]
    return "{0:.2f}".format(total)