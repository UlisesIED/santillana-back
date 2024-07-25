from rest_framework.serializers import ModelSerializer

from catalogos.models import Cat_juegos

class Cat_juegos_serializer(ModelSerializer):
    class Meta:
        model = Cat_juegos
        fields = '__all__'