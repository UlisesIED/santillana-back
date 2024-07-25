from django.db import models

class Cat_juegos(models.Model):
    descripcion = models.CharField(unique=True, max_length=128)
