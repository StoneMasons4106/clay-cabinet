from django.contrib import admin
from .models import Content, BlackList

# Register your models here.

class ContentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

    fields = (
        'name',
        'contact_blurb',
        'google_maps_link',
        'address',
        'email',
        'phone',
    )

    ordering = ('name',)


class BlackListAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

    fields = (
        'name',
        'first_name',
        'last_name',
        'email',
    )

    ordering = ('name',)


admin.site.register(Content, ContentAdmin)
admin.site.register(BlackList, BlackListAdmin)