from django.contrib import admin
from .models import Content

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


admin.site.register(Content, ContentAdmin)