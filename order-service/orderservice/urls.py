
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from orders.views import OrderViewSet

# Create a router and register the OrderViewSet with it
router = DefaultRouter()
router.register(r'orders', OrderViewSet)

# Include the router URLs in the urlpatterns
urlpatterns = [
    path('orders/', include(router.urls)),
]
