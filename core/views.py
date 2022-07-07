# from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
# from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from core.models import Products, Category
from core.serializers import ProductSerializer, CategorySerializer
from django_filters import rest_framework as filters


class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Products
        fields = ['category']


class ProductView(ModelViewSet):
    queryset = Products.objects.all().order_by('-id')
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category']
    filterset_class = ProductFilter
    search_fields = ['name', 'description']
    ordering_fields = ['price']


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'


