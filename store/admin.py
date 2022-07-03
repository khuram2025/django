from django.contrib import admin

# Register your models here.
from store.models import Category, Product, City, Seller

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'seller', 'slug', 'price', 'video','created_at', 'updated_at', 'in_stock',]
    list_filter = ['created_at', 'is_active', 'in_stock']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
   
@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['name','created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']