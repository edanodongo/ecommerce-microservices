# from django.contrib import admin
# from django.urls import path
# from orders.views import OrderListCreateView

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/orders/', OrderListCreateView.as_view(), name='order-list-create'),
# ]


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
