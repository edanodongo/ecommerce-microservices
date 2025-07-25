from django.db import models

# This file defines the Product model which represents the product data in the database.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    inventory = models.PositiveIntegerField()

    def __str__(self):
        return self.name

