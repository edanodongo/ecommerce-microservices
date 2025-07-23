from rest_framework import serializers
from .models import Order

# Order Serializer
# This serializer is used to convert Order model instances into JSON format and vice versa.
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
