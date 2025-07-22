# from django.db import models

# # Payment Status Choices
# # These choices represent the different states a payment can be in.
# PAYMENT_STATUS = [
#     ('PENDING', 'Pending'),
#     ('COMPLETED', 'Completed'),
#     ('FAILED', 'Failed'),
# ]

# # Payment Model
# # This model represents a payment transaction in the system.
# class Payment(models.Model):
#     order_id = models.IntegerField()
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     status = models.CharField(max_length=10, choices=PAYMENT_STATUS, default='PENDING')
#     transaction_id = models.CharField(max_length=100, blank=True, null=True)
#     paid_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Payment for Order {self.order_id}"



from django.db import models

# Payment Model
# This model represents a payment transaction in the system.
class Payment(models.Model):
    order_id = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default='initiated')
    payment_method = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
