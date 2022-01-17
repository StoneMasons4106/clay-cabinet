from django.contrib import admin
from .models import HomePagePicture, Testimonial

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


class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

    fields = (
        'name',
        'image',
        'testimonial',
    )

    ordering = ('name',)


admin.site.register(HomePagePicture, HomePagePictureAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
