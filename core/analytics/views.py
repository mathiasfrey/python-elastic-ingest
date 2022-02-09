from rest_framework import viewsets

from analytics.models import Entity, Channel, Product, SalesPerformance
from analytics.serializers import EntitySerializer, ChannelSerializer, ProductSerializer, SalesPerformanceSerializer

class EntityViewSet(viewsets.ModelViewSet):
    serializer_class = EntitySerializer
    queryset = Entity.objects.all()

class ChannelViewSet(viewsets.ModelViewSet):
    serializer_class = ChannelSerializer
    queryset = Channel.objects.all()

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class SalesPerformanceViewSet(viewsets.ModelViewSet):
    serializer_class = SalesPerformanceSerializer
    queryset = SalesPerformance.objects.all()