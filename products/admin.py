from django.contrib import admin

from .models import Product
from .models import Variation

# Register your models here.
admin.site.register(Product)
admin.site.register(Variation)