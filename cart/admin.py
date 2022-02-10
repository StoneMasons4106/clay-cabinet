from django.contrib import admin
from .models import UserCart

# Register your models here.

class UserCartAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'cart',
    )

    ordering = ('user',)

admin.site.register(UserCart, UserCartAdmin)
