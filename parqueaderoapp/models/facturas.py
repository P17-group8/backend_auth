from django.db import models
from .user import User
from .plazas import Plazas
from .usuarios import Usuarios


class Factura(models.Model):
    idfactura = models.AutoField(primary_key=True)
    placa = models.CharField(max_length=30)
    costo_total = models.DecimalField(max_digits=5, decimal_places=2,default=0)
    id_plazask = models.ForeignKey(Plazas, related_name='facidplazas', on_delete=models.CASCADE)  
    tipo_vehiculo = models.CharField(max_length=30)   
    fecha_entrada = models.DateTimeField()
    fecha_salida = models.DateTimeField()  
    ususariok = models.ForeignKey(Usuarios, related_name='faciduser', on_delete=models.CASCADE)
    
  