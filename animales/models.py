from django.db import models
import uuid

# Create your models here.
class Especie(models.Model):
    id      = models.IntegerField(primary_key=True, unique=True) 
    especie = models.CharField(max_length=50, verbose_name='Especie de animal')

    def __str__(self):
        return f"{self.especie}"

class Animal(models.Model):
    uuid          = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    nombre        = models.CharField(max_length=100, verbose_name='Nombre')
    edad          = models.IntegerField(verbose_name='Edad')
    descripcion   = models.TextField(null=True, blank=True, verbose_name='Descripción')
    fecha_ingreso = models.DateTimeField(auto_now_add=True, verbose_name="Fecha ingreso")
    disponible    = models.BooleanField(default=True)
    especie       = models.ForeignKey(Especie, on_delete=models.CASCADE, null=True, blank=True, related_name='animales')

    def __str__(self):
        return f"{self.id} - {self.nombre}"