from django.shortcuts import render
from .models import Product, Category

# Create your views here.   
def all_products(request):
    return render(request, 'store/all_products.html')

