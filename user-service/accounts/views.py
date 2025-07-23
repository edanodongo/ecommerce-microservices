from django.shortcuts import render
from rest_framework import generics
from .models import CustomUser
from .serializers import RegisterSerializer

# View to handle user list and creation
class UserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer


# from rest_framework import generics, permissions
# from rest_framework.response import Response
# from rest_framework.authtoken.models import Token
# from rest_framework.views import APIView
# from django.contrib.auth import get_user_model
# from rest_framework import status
# from .serializers import RegisterSerializer
# from django.contrib.auth.password_validation import validate_password
# from django.core.exceptions import ValidationError

# User = get_user_model()

# # View to handle user registration
# class RegisterView(APIView):
#     permission_classes = [permissions.AllowAny]

#     def post(self, request):
#         data = request.data
#         try:
#             validate_password(data.get("password"))
#         except ValidationError as e:
#             return Response({"error": e.messages}, status=status.HTTP_400_BAD_REQUEST)

#         if User.objects.filter(username=data.get("username")).exists():
#             return Response({"error": "Username already exists"}, status=400)
#         if User.objects.filter(email=data.get("email")).exists():
#             return Response({"error": "Email already exists"}, status=400)

#         user = User.objects.create_user(
#             username=data.get("username"),
#             email=data.get("email"),
#             password=data.get("password")
#         )
#         token = Token.objects.create(user=user)
#         return Response({
#             "user": RegisterSerializer(user).data,
#             "token": token.key
#         }, status=201)

