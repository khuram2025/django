from itertools import product
from django.shortcuts import render, get_object_or_404
from .models import Product, Category


# Create your views here.   
def all_products(request):
    products = Product.objects.all()
    return render(request, 'front/home.html', {'products': products})


def categories(request):
    return{
        'categories': Category.objects.all()
    }

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'home/product_detail.html', {'product': product})
