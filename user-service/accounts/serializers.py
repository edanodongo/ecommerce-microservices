# from rest_framework import serializers
# from .models import CustomUser

# # Serializers for the CustomUser model
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['id', 'username', 'email']


from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password

# Serializers for the CustomUser model
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
