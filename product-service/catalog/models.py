# from django.db import models

# # This file defines the Product model which represents the product data in the database.
# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=8, decimal_places=2)
#     inventory = models.IntegerField()

#     def __str__(self):
#         return self.name


from django.db import models

# This file defines the Product model which represents the product data in the database.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
