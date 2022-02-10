from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserCart(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cart = models.CharField(max_length=2000, null=True, blank=True)
    
    def __str__(self):
        return self.user.username