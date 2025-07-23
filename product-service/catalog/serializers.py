# projects/ecommerce-microservices/product-service/catalog/serializers.py
from rest_framework import serializers
from .models import Product

# Serializers define the API representation.
# This serializer will convert the Product model instances into JSON format
# and validate incoming data for creating or updating Product instances.
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
