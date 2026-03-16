from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from core.views import (ImportTaskStatusView, ManufacturerViewSet,
                        OrderViewSet, ProductViewSet, UploadProductsView)

router = DefaultRouter()
router.register(r'manufacturers', ManufacturerViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    url(r'^upload-products/$', UploadProductsView.as_view(), name='upload-products'),
    url(r'^import-tasks-status/(?P<task_id>[^/]+)/$', ImportTaskStatusView.as_view(), name='import-task-status'),
]

urlpatterns += router.urls
