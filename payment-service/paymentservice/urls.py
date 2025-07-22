# from django.contrib import admin
# from django.urls import path
# from payments.views import PaymentListCreateView

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/payments/', PaymentListCreateView.as_view(), name='payment-list-create'),
# ]



from django.urls import path, include
from rest_framework.routers import DefaultRouter
from payments.views import PaymentViewSet

# Create a router and register the PaymentViewSet with it
router = DefaultRouter()
router.register(r'payments', PaymentViewSet)

# Include the router URLs in the urlpatterns
urlpatterns = [
    path('payments/', include(router.urls)),
]
