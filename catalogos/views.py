from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from catalogos.models import Cat_juegos
from catalogos.api.serializer import Cat_juegos_serializer

class Cat_juegos_view_set(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = Cat_juegos_serializer
    queryset = Cat_juegos.objects.all()
    
