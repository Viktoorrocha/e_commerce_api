# app/urls.py

from django.contrib import admin
from django.urls import path, include, re_path # Importe 'include' aqui!
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView # Inclua Redoc se quiser

# Importação para JWT 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

# Importação para Swagger UI/Spectacular
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),

    # URLs para o DRF Spectacular (Documentação OpenAPI/Swagger)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'), # Opcional: Redoc

    #URLs para autenticação JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # É crucial que as URLs dos seus apps estejam incluídas!
    path('api/', include('products.urls')), # Isso vai incluir '/api/categories/' e '/api/products/'
]