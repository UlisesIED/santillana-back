from django.db import models
from catalogos.models import Cat_juegos

class Marcador_juego(models.Model):
    id_juego = models.ForeignKey(Cat_juegos, on_delete=models.CASCADE)
    marcador = models.CharField(max_length=256, null=False)
    fecha_registro = models.TimeField(auto_now=True)