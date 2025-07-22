# from rest_framework import generics
# from .models import Payment
# from .serializers import PaymentSerializer

# # Payment List and Create View
# # This view allows listing all payments and creating a new payment.
# class PaymentListCreateView(generics.ListCreateAPIView):
#     queryset = Payment.objects.all()
#     serializer_class = PaymentSerializer


from rest_framework import viewsets
from .models import Payment
from .serializers import PaymentSerializer

# Payment ViewSet
# This view handles listing all payments and creating a new payment.
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    