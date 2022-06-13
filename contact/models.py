from django.db import models

# Create your models here.

class Content(models.Model):

    name = models.CharField(max_length=254)
    contact_blurb = models.CharField(max_length=500)
    google_maps_link = models.URLField(max_length=2000, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return self.name


class BlackList(models.Model):

    name = models.CharField(max_length=254)
    first_name = models.CharField(max_length=254, blank=True, null=True)
    last_name = models.CharField(max_length=254, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)

    def __str__(self):
        return self.name