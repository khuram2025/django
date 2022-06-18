from django.contrib import admin

# Register your models here.
from .models import Seller
from store import models as store_models

admin.site.register(Seller)

