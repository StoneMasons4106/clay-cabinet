from django import template
from products.models import Category

register = template.Library()

@register.filter(name='categories')
def categories(all_categories):
    all_categories = Category.objects.values()
    return all_categories