from django.db import models

# Create your models here.

class HomePagePicture(models.Model):
    name = models.CharField(max_length=254)
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=254, null=True, blank=True)
    description = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=254)
    image = models.ImageField(null=True, blank=True)
    testimonial = models.TextField(max_length=2048)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class Content(models.Model):
    name = models.CharField(max_length=254)
    gallery_title = models.CharField(max_length=254)
    gallery_text = models.CharField(max_length=254)
    video_title = models.CharField(max_length=254)
    video_content = models.CharField(max_length=100000, null=True, blank=True)
    video_text = models.CharField(max_length=254)
    testimonial_title = models.CharField(max_length=254)
    testimonial_text = models.CharField(max_length=254)

    def __str__(self):
        return self.name