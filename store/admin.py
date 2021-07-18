from django.contrib import admin

from .models import (
    Supplier,
    Product,
    Inventory,
)

admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(Inventory)
