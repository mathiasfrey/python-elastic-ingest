from django.contrib import admin
from analytics.models import Sales, SalesPerformance, Channel, Entity, Product

admin.site.register(Sales)
admin.site.register(SalesPerformance)
admin.site.register(Channel)
admin.site.register(Entity)
admin.site.register(Product)