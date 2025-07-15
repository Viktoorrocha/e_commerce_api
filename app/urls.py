# app/urls.py

from django.contrib import admin
from django.urls import path, include # Importe 'include' aqui!
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView # Inclua Redoc se quiser

urlpatterns = [
    path('admin/', admin.site.urls),

    # URLs para o DRF Spectacular (Documentação OpenAPI/Swagger)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'), # Opcional: Redoc

    # Inclua as URLs do seu app 'products' aqui
    # É crucial que as URLs dos seus apps estejam incluídas!
    path('api/', include('products.urls')), # Isso vai incluir '/api/categories/' e '/api/products/'
]