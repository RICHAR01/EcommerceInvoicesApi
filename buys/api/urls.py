from django.urls import path, include
from rest_framework.routers import DefaultRouter
from buys.api.views import SupplierViewSet, BuyHeaderViewSet, BuyDetailViewSet

router = DefaultRouter()
router.register(r'suppliers', SupplierViewSet)
router.register(r'buy-headers', BuyHeaderViewSet)
router.register(r'buy-details', BuyDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
