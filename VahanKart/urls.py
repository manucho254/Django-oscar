from django.apps import apps
from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Vahankart API",
      default_version='v1',
      description="Api description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@admin.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    # The Django admin is not officially supported; expect breakage.
    # Nonetheless, it's often useful for debugging.
    path('admin/', admin.site.urls),
    path('', include(apps.get_app_config('oscar').urls[0])),
    path("api/", include("oscarapi.urls")),
    path('swagger.json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
