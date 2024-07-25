from rest_framework.routers import DefaultRouter

from juegos.views import Marcador_juego_view_set

router_marcador_juego = DefaultRouter()
router_marcador_juego.register(
    prefix='juegos',
    basename='juegos',
    viewset=Marcador_juego_view_set
)