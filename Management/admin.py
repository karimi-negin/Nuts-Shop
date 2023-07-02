from django.contrib import admin
from .models import *
from django.utils.html import format_html
from .models import Product

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(City)
admin.site.register(Inventory)
admin.site.register(InventoryProduct)
admin.site.register(Order)
