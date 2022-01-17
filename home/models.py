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
    testimonal = models.TextField(max_length=2048)

    def __str__(self):
        return self.name