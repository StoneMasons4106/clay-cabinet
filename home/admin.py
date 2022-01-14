from django.contrib import admin
from .models import HomePagePicture

class HomePagePictureAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'title',
        'description',
    )

    fields = (
        'name',
        'image',
        'title',
        'description',
    )

    ordering = ('name',)

admin.site.register(HomePagePicture, HomePagePictureAdmin)
