from types import CoroutineType
from django.db import models
from store import models as store_models


# Create your models here.
class Seller(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    location = models.ForeignKey(store_models.City, on_delete=models.CASCADE, blank=True,),
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='seller_profile_images', blank=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
