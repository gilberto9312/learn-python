from django.db import models
from django.urls import reverse

class Periodo(models.Model):
    nombre = models.CharField(max_length=100)
    fechaInicio = models.DateTimeField()
    fechaFin = models.DateTimeField()
    status = models.BooleanField()
    fechaRegistro = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now_add=True)
    entidadesId = models.IntegerField(blank=True, null = True)

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('photo-list')