from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from embed_video.fields import EmbedVideoField



# Create Category Model
class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)    # slug field    will be used to generate a URL
    image = models.FileField(upload_to='category_images', blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'categories'

   
    def get_absolute_url(self):
        return reverse("store:category_list", args = [self.slug])


    

    def __str__(self):
        return self.name

#Create City Model

class City(models.Model):
    province = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, default = "Province")
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'cities'

    def __str__(self):
        return self.name

class Seller(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    mobile_num = models.CharField(max_length=255),
    profile_pic = models.ImageField(upload_to='seller_images/', blank=True),
    bio = models.TextField(blank=True),
    facebook = models.URLField(blank=True),
    twitter = models.URLField(blank=True),
    status = models.BooleanField(default=True)
    rank = models.IntegerField(default=0)
    city = models.ForeignKey(City, on_delete=models.SET_DEFAULT, blank=True, null=True, default = "City")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


#create Product Model
class Product(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True, default="Test")
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='product_creator', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, db_index=True)
    seller = models.ForeignKey(Seller, on_delete=models.DO_NOTHING,)
    mobile_num = models.CharField(max_length=255) 
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    video = EmbedVideoField()
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Products'

    def get_absolute_url(self):
        return reverse("store:product_detail", args = [self.slug])
    

    def __str__(self):
        return self.title


