from django.urls import path

from . import views 

app_name = 'seller'

urlpatterns = [
    path('become_seller/', views.become_seller, name='become_seller'),
]
