from django.contrib import admin
from django.urls import path
from payments.views import PaymentListCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/payments/', PaymentListCreateView.as_view(), name='payment-list-create'),
]
