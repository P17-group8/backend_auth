from parqueaderoapp.models.tarifa import Tarifa
from rest_framework import serializers
class TarifaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarifa
        fields = ['precio_x_minuto', 'precio_fraccion', 'fraccion']