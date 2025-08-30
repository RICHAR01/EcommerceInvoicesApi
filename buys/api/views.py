from rest_framework import viewsets
from buys.models import Supplier, BuyHeader, BuyDetail
from buys.api.serializers import SupplierSerializer, BuyHeaderSerializer, BuyDetailSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class BuyHeaderViewSet(viewsets.ModelViewSet):
    queryset = BuyHeader.objects.all()
    serializer_class = BuyHeaderSerializer

class BuyDetailViewSet(viewsets.ModelViewSet):
    queryset = BuyDetail.objects.all()
    serializer_class = BuyDetailSerializer
