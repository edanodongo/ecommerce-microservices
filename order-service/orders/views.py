from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer

# Order List and Create View
# This view allows listing all orders and creating a new order.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
