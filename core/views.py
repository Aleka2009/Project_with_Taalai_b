# from rest_framework import generics
from django.contrib.auth.models import User
from django.db.models import Prefetch, F, Count
from rest_framework.filters import SearchFilter, OrderingFilter
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from core.models import Products, Category
from core.permissions import ProductPermission
from core.serializers import ProductSerializer, CategorySerializer
from django_filters import rest_framework as filters


class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Products
        fields = ['category']


class ProductView(ModelViewSet):
    # queryset = Products.objects.all().order_by('-id')
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category']
    filterset_class = ProductFilter
    search_fields = ['name', 'description']
    ordering_fields = ['price']
    permission_classes = (ProductPermission,)

    def get_queryset(self):
        queryset = Products.objects.annotate(
            category_name=F('category__name'),
            owner_name=F('user__username')
        ).order_by('-id')
        return queryset

    # Один из оптимальных вариантов прямого запроса
    # def get_queryset(self):
    #     queryset = Products.objects.prefetch_related(
    #         'category',
    #         Prefetch('user', queryset=User.objects.only('username', 'id'))
    #     ).order_by('-id')
    #     return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'

    def get_queryset(self):
        queryset = Category.objects.annotate(
            product_count=Count('products')
        )
        return queryset
