from rest_framework import serializers

from core.models import Products


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'name', 'price', 'description', 'image')


# class ProductDetailCreateUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Products
#         fields = ('id', 'name', 'price', 'description', 'image')

