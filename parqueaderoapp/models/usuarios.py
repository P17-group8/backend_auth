from django.db import models

class Usuarios(models.Model):
    idusuarios = models.AutoField(primary_key=True)   
    nombres = models.CharField(max_length=30)  
    apellidos = models.CharField(max_length=30)   
    user = models.CharField(max_length=30)  
    password = models.CharField(max_length=30) 
    tipo_identificacion = models.CharField(max_length=30) 
    identificacion = models.CharField(max_length=30) 
    correo = models.CharField(max_length=30) 
    