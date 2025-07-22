# from django.contrib import admin
# from django.urls import path
# from catalog.views import ProductListCreateView

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/products/', ProductListCreateView.as_view(), name='product-list-create'),
# ]


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from catalog.views import ProductViewSet

# Create a router and register the ProductViewSet with it
router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('catalog/', include(router.urls)),
]
