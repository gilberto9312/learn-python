from django.db import models
from django.urls import reverse





class Periodo(models.Model):
    nombre = models.CharField(max_length=100)
    fechaInicio = models.DateTimeField()
    fechaFin = models.DateTimeField()
    status = models.BooleanField()
    fechaRegistro = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('photo-list')

class Entidad(models.Model):
    nombre = models.CharField(max_length=100)
    ruc = models.CharField(max_length=50)
    direcion = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    canton = models.CharField(max_length=100)
    parroquia = models.CharField(max_length=100)
    periodo = models.ManyToManyField(Periodo, blank=True, null = True)
    fechaRegistro = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now_add=True)