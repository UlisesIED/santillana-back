from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import( 
    SpectacularAPIView, 
    SpectacularSwaggerView,
    SpectacularRedocView,
)

from catalogos.api.router import router_cat_juegos
from juegos.api.router import router_marcador_juego

urlpatterns = [
    path('admin/', admin.site.urls),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/",SpectacularSwaggerView.as_view( url_name="schema"),
        name="swagger-ui",
    ),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path("api/", include(router_cat_juegos.urls)),
    path("api/", include(router_marcador_juego.urls)),
]
