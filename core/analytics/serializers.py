from html import entities
from rest_framework import serializers

from analytics.models import Entity, Channel, Product, SalesPerformance


class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = '__all__'


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class SalesPerformanceSerializer(serializers.ModelSerializer):
    
    # skip this because nested serializers are a hazzle when trying
    # to write data 
    # https://www.django-rest-framework.org/api-guide/serializers/#dealing-with-nested-objects
    # entity = EntitySerializer()
    # channel = ChannelSerializer()
    # product = ProductSerializer()

    class Meta:
        model = SalesPerformance
        fields = '__all__'