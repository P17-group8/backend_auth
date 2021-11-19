from django.db import models

class Tarifa(models.Model):
    idtarifa = models.AutoField(primary_key=True)
    precio_x_minuto = models.DecimalField(max_digits=5, decimal_places=2,default=0)  
    precio_fraccion = models.DecimalField(max_digits=5, decimal_places=2,default=0)  
    fraccion = models.IntegerField(default=0)