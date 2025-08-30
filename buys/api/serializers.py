from rest_framework import serializers
from buys.models import Supplier, BuyHeader, BuyDetail

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class BuyDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = BuyDetail
        fields = ['id', 'product', 'quantity', 'supply_price', 'subtotal', 'discount', 'total']

class BuyHeaderSerializer(serializers.ModelSerializer):
    buy_details = BuyDetailSerializer(many=True)

    class Meta:
        model = BuyHeader
        fields = ['id', 'buy_date', 'observation', 'invoice', 'invoice_date', 'supplier', 'subtotal', 'discount', 'total', 'buy_details']

    def create(self, validated_data):
        buy_details_data = validated_data.pop('buy_details')
        buy_header = BuyHeader.objects.create(**validated_data)
        for buy_detail_data in buy_details_data:
            BuyDetail.objects.create(buy=buy_header, **buy_detail_data)
        return buy_header

    def update(self, instance, validated_data):
        buy_details_data = validated_data.pop('buy_details', None)
        instance.buy_date = validated_data.get('buy_date', instance.buy_date)
        instance.observation = validated_data.get('observation', instance.observation)
        instance.invoice = validated_data.get('invoice', instance.invoice)
        instance.invoice_date = validated_data.get('invoice_date', instance.invoice_date)
        instance.supplier = validated_data.get('supplier', instance.supplier)
        instance.subtotal = validated_data.get('subtotal', instance.subtotal)
        instance.discount = validated_data.get('discount', instance.discount)
        instance.total = validated_data.get('total', instance.total)
        instance.save()

        if buy_details_data is not None:
            # Delete old buy details
            instance.buy_details.all().delete()

            # Create new buy details
            for buy_detail_data in buy_details_data:
                BuyDetail.objects.create(buy=instance, **buy_detail_data)

        return instance
