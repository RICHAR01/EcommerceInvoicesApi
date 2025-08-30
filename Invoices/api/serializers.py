from rest_framework import serializers
from Invoices.models import Client, SaleHeader, SaleDetail

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class SaleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleDetail
        fields = ['product', 'quantity', 'unit_price', 'line_subtotal', 'line_discount', 'line_total']

class SaleHeaderSerializer(serializers.ModelSerializer):
    sale_details = SaleDetailSerializer(many=True)

    class Meta:
        model = SaleHeader
        fields = ['id', 'client', 'invoice_date', 'subtotal', 'discount', 'total_amount', 'invoice_status', 'paid_status', 'sale_details']

    def create(self, validated_data):
        sale_details_data = validated_data.pop('sale_details')
        sale_header = SaleHeader.objects.create(**validated_data)
        for sale_detail_data in sale_details_data:
            SaleDetail.objects.create(sale=sale_header, **sale_detail_data)
        return sale_header

    def update(self, instance, validated_data):
        sale_details_data = validated_data.pop('sale_details', None)
        instance.client = validated_data.get('client', instance.client)
        instance.invoice_date = validated_data.get('invoice_date', instance.invoice_date)
        instance.subtotal = validated_data.get('subtotal', instance.subtotal)
        instance.discount = validated_data.get('discount', instance.discount)
        instance.total_amount = validated_data.get('total_amount', instance.total_amount)
        instance.invoice_status = validated_data.get('invoice_status', instance.invoice_status)
        instance.paid_status = validated_data.get('paid_status', instance.paid_status)
        instance.save()

        if sale_details_data is not None:
            # Delete old sale details
            instance.sale_details.all().delete()

            # Create new sale details
            for sale_detail_data in sale_details_data:
                SaleDetail.objects.create(sale=instance, **sale_detail_data)

        return instance
