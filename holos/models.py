from django.db import models
import uuid

# Create your models here.
class Generacion(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Generación')

    def __str__(self):
        return f"gen - {self.nombre}"

class Holomem(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    descripcion = models.TextField(blank=True, null=True, verbose_name='Descripción')
    cant_seguidores = models.IntegerField(verbose_name='Cantidad seguidores YouTube')
    fecha_debut = models.DateField(verbose_name='Fecha de Debut')
    activo = models.BooleanField(default=True, verbose_name='Activo')

    generacion = models.ForeignKey(Generacion, on_delete=models.CASCADE, null=True, blank=True, related_name='holomiembros')

    def __str__(self):
        return f"nombre - {self.nombre}"

