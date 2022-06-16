from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



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



#create Product Model
class Product(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True, default="Test")
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='product_creator', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, db_index=True)
    seller = models.CharField(max_length=255, default='admin')
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
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


