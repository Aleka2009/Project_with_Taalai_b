from rest_framework import serializers

from core.models import Products, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'name', 'price', 'description', 'image', 'category')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')

# class ProductDetailCreateUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Products
#         fields = ('id', 'name', 'price', 'description', 'image')

