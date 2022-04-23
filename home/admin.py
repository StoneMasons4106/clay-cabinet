from django.contrib import admin
from .models import HomePagePicture, Testimonial, Content

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


class ContentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

    fields = (
        'name',
        'banner_text',
        'gallery_title',
        'gallery_text',
        'video_title',
        'video_content',
        'video_text',
        'testimonial_title',
        'testimonial_text',
    )

    ordering = ('name',)


admin.site.register(HomePagePicture, HomePagePictureAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Content, ContentAdmin)
