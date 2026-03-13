from rest_framework.routers import DefaultRouter

from .views import ManufacturerViewSet, OrderViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'manufacturers', ManufacturerViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = router.urls
