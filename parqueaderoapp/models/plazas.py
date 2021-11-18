from django.db import models

class Plazas(models.Model):
    idplazas = models.AutoField(primary_key=True)
    tipo_plaza = models.CharField(max_length=30)    
    codigo_plaza = models.CharField(max_length=30)
    estado = models.CharField(max_length=30)  