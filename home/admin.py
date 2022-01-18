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
        'date',
    )

    fields = (
        'name',
        'date',
        'image',
        'testimonial',
    )

    ordering = ('date',)


admin.site.register(HomePagePicture, HomePagePictureAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
