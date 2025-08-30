from rest_framework import viewsets
from Invoices.models import Client, SaleHeader, SaleDetail
from Invoices.api.serializers import ClientSerializer, SaleHeaderSerializer, SaleDetailSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class SaleHeaderViewSet(viewsets.ModelViewSet):
    queryset = SaleHeader.objects.all()
    serializer_class = SaleHeaderSerializer

class SaleDetailViewSet(viewsets.ModelViewSet):
    queryset = SaleDetail.objects.all()
    serializer_class = SaleDetailSerializer
