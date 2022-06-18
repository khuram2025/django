from django.shortcuts import render

# Create your views here.

def become_seller(request):
    return render(request, 'front/page-register.html')
