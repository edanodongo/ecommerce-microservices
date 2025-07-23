# payments/views.py
from rest_framework import viewsets
from .models import Payment
from .serializers import PaymentSerializer

# Payment ViewSet
# This view handles listing all payments and creating a new payment.
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    