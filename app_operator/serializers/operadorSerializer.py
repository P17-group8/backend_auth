from app_operator.models.operador   import Operador
from rest_framework                 import serializers
#from rest_framework.relations import PrimaryKeyRelatedField


class OperadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operador
        fields = ['id','nombre_operador','apellido_operador','username','password','identificacion','email']
    
    def to_representation(self, obj):
        operador = Operador.objects.get(id=obj.id)
        return {
            'id'                :operador.id,
            'nombre'            :operador.nombre_operador,
            'apellido'          :operador.apellido_operador,
            'username'          :operador.username,
            'identificacion'    :operador.identificacion,
            'email'             :operador.email
        }   