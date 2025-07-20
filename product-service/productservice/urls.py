from django.contrib import admin
from django.urls import path
from catalog.views import ProductListCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/', ProductListCreateView.as_view(), name='product-list-create'),
]
