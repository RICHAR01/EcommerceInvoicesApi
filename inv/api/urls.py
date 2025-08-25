from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet,
    SubcategoryViewSet,
    BrandViewSet,
    MeasureUnitViewSet,
    ProductViewSet
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubcategoryViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'measure-units', MeasureUnitViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]