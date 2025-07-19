from rest_framework import serializers
from .models import CustomUser

# Serializers for the CustomUser model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email']
