from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from analytics.models import Sales, SalesPerformance, Channel, Entity, Product

@registry.register_document
class SalesDocument(Document):

    class Index:
        name = 'sales'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = Sales
        fields = [
            'date',
            'product',
            'count',
        ]
    
@registry.register_document
class SalesPerformanceDocument(Document):

    entity = fields.ObjectField(properties={
        #'id': fields.IntegerField(),
        'name': fields.KeywordField(),
    })
    channel = fields.ObjectField(properties={
        #'id': fields.IntegerField(),
        'name': fields.KeywordField(),
    })
    product = fields.ObjectField(properties={
        #'id': fields.IntegerField(),
        'name': fields.KeywordField(),
    })

    class Index:
        name = 'salesperformance'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = SalesPerformance
        fields = [
            'date',
            'contracts',
            'volume',
        ]
        # related_models = [Entity, Channel, Product]
