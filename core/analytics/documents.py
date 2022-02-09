from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from analytics.models import Sales

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