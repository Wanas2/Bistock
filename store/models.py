from django.db import models

from datetime import datetime

from users.models import User

class Supplier(models.Model):
    name = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    tel = models.CharField(max_length=30)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    designation = models.CharField(max_length=255, unique=True)
    buying_price = models.PositiveIntegerField()
    selling_price = models.PositiveIntegerField()
    category = models.CharField(max_length=30)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.designation

class Inventory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    qty = models.IntegerField(default=0)
    created_at = models.DateField(default=datetime.now())

    def __str__(self):
        return "{} {} - {}".format(self.product, self.supplier, self.qty)
