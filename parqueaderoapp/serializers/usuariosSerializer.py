from parqueaderoapp.models.usuarios import Usuarios
from rest_framework import serializers
class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ['nombres', 'apellidos', 'user', 'password', 'tipo_identificacion', 'identificacion', 'correo']