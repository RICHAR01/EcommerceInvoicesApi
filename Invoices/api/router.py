from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Invoices.api.views import ClientViewSet, SaleHeaderViewSet, SaleDetailViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'sale-headers', SaleHeaderViewSet)
router.register(r'sale-details', SaleDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
