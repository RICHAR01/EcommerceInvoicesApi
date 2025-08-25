from rest_framework import viewsets
from .models import Category, Subcategory, Brand, MeasureUnit, Product
from .serializers import (
    CategorySerializer,
    SubcategorySerializer,
    BrandSerializer,
    MeasureUnitSerializer,
    ProductSerializer
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class MeasureUnitViewSet(viewsets.ModelViewSet):
    queryset = MeasureUnit.objects.all()
    serializer_class = MeasureUnitSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
