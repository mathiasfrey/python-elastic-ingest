from django.urls import path, include
from rest_framework import routers

from analytics.views import EntityViewSet, ChannelViewSet, ProductViewSet, SalesPerformanceViewSet

router = routers.DefaultRouter()
router.register(r'entity', EntityViewSet)
router.register(r'channel', ChannelViewSet)
router.register(r'product', ProductViewSet)
router.register(r'salesperformance', SalesPerformanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]