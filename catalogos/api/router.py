from rest_framework.routers import DefaultRouter

from catalogos.views import Cat_juegos_view_set

router_cat_juegos = DefaultRouter()
router_cat_juegos.register(
    prefix= 'cat_juegos',
    basename='cat_juegos',
    viewset=Cat_juegos_view_set
)