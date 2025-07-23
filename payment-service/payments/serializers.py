
from rest_framework import serializers
from .models import Payment

# Payment Serializer
# This serializer is used to convert Payment model instances into JSON format and vice versa.
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
