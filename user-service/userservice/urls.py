
from django.contrib import admin
from django.urls import path, include
from accounts.views import UserListCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', UserListCreateView.as_view(), name='user-list-create'),
]
