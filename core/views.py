from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.models import Products
from core.serializers import ProductSerializer


class ProductView(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


