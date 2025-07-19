from django.shortcuts import render
from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer

# View to handle user list and creation
class UserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
