import requests
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer

PRODUCT_SERVICE_URL = "http://product-service:8001/catalog/products/"

from .utils.jwt import create_service_token


# Order ViewSet
# This view handles listing all orders and creating a new order.
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        product_id = request.data.get("product_id")
        quantity = int(request.data.get("quantity", 0))

        # Fetch product info from Product Service
        try:            
            headers = {
                "Authorization": f"Bearer {create_service_token()}"
            }
            product_response = requests.get(f"{PRODUCT_SERVICE_URL}{product_id}/", headers=headers)
            if product_response.status_code != 200:
                return Response({"error": "Product not found"}, status=404)

            product = product_response.json()
            available_quantity = int(product.get("quantity", 0))
            if quantity > available_quantity:
                return Response({"error": "Not enough stock"}, status=400)

        except Exception as e:
            return Response({"error": f"Error fetching product: {str(e)}"}, status=500)

        # Create the order
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
