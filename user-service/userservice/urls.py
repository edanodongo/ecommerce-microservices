
from django.contrib import admin
from django.urls import path, include
from accounts.views import UserListCreateView
from accounts.views import RegisterView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', UserListCreateView.as_view(), name='user-list-create'),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', obtain_auth_token, name='login'),
]

