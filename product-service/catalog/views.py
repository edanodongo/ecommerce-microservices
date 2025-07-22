# from rest_framework import generics
# from .models import Product
# from .serializers import ProductSerializer

# # This view handles listing all products and creating a new product.
# class ProductListCreateView(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer



from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

# This view handles listing all products and creating a new product.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
