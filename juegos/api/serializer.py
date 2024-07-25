from rest_framework.serializers import ModelSerializer

from juegos.models import Marcador_juego
from catalogos.api.serializer import Cat_juegos_serializer

class Marcador_juego_serializer(ModelSerializer):
    id_juego = Cat_juegos_serializer(read_only = True)
    class Meta:
        model = Marcador_juego
        fields = '__all__'