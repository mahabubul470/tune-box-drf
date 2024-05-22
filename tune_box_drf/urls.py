from django.urls import path, include
from core.views import CustomTokenDestroyView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/token/logout/', CustomTokenDestroyView.as_view(), name='custom_token_destroy'),
    path('api/auth/', include('djoser.urls.authtoken')),
    path('api/', include('core.urls')),
]
