from django.contrib import admin
from django.urls import path
from orders.views import OrderListCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/orders/', OrderListCreateView.as_view(), name='order-list-create'),
]
