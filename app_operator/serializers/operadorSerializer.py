from rest_framework import serializers
from app_operator.models.operador import Operador
from rest_framework.relations import PrimaryKeyRelatedField


class OperadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operador
        fields = ['id','nombre_operador','apellido_operador','user_operador','password','identificacion','email']
    def create(self, validated_data):
        userInstance = Operador.objects.create(**validated_data)
        return userInstance
    def to_representation(self, obj):
        user = Operador.objects.get(id=obj.id)
        return {
            'id':user.id,
            'nombre':user.nombre_operador,
            'apellido':user.apellido_operador,
            'userr':user.user_operador,
            'password':user.password,
            'identificacion':user.identificacion,
            'email':user.email
        }   