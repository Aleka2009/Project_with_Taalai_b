from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.models import Products, Category
from core.serializers import ProductSerializer, CategorySerializer


class ProductView(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'


