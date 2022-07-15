from django.contrib.auth.models import User
from rest_framework import serializers
from core.models import Products, Category


class ProductSerializer(serializers.ModelSerializer):
    # Один из оптимальных вариантов прямого запроса
    # category_name = serializers.SerializerMethodField()
    # owner_name = serializers.SerializerMethodField()

    category_name = serializers.CharField(read_only=True)
    owner_name = serializers.CharField(read_only=True)

    class Meta:
        model = Products
        fields = ('id', 'name', 'price', 'description', 'image', 'category', 'user', 'category_name',
                  'owner_name')
    extra_kwargs = {'user': {'read_only': True}}

    # Один из оптимальных вариантов прямого запроса
    # def get_category_name(self, obj):
    #     if obj.category:
    #         return obj.category.name
    #
    # def get_owner_name(self, obj: Products):  # Аннотация obj: Products
    #     if obj.user:
    #         return obj.user.username

 # '''Связь пользователя с созданными продуктами. Нагрузка на базы данных таким способом.'''
     # def create(self, validated_data):
     #    product = Products.objects.create(**validated_data)
     #    product.user = self.context.get('request').user
     #    product.save()
     #    return product


class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = '__all__'

# class ProductDetailCreateUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Products
#         fields = ('id', 'name', 'price', 'description', 'image')

