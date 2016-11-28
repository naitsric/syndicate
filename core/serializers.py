from rest_framework import serializers

from core.models import Product, Investor, Purchase


class ProductSerializer(serializers.Serializer):
    class Meta:
        model = Product

class InvestorSerializer(serializers.Serializer):
    class Meta:
        model = Investor

class PurchaseSerializer(serializers.Serializer):
    class Meta:
        model = Purchase