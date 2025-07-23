from django.db import models

# Order Status Choices
# These choices can be used to represent the status of an order in the system.
ORDER_STATUS = [
    ('PENDING', 'Pending'),
    ('CONFIRMED', 'Confirmed'),
    ('SHIPPED', 'Shipped'),
    ('CANCELLED', 'Cancelled'),
]

# Order Model
# This model represents an order in the e-commerce system.
class Order(models.Model):
    user_id = models.IntegerField()  # reference to User service
    product_id = models.IntegerField()  # reference to Product service
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=ORDER_STATUS, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id}"
        # Optionally, you can also return the product info in the response
        # return f"Order #{self.id} for Product ID {self.product_id} by User ID {self.user_id}"