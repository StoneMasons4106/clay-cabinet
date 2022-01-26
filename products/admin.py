from django.contrib import admin
from .models import Product, Category, Content

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'id',
        'name',
        'category',
        'price',
        'description',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class ContentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Content, ContentAdmin)