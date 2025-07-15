#products/urls.py 

from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet) # URL base: /api/categories/
router.register(r'products', ProductViewSet) # URL base: /api/products/


urlpatterns = router.urls
