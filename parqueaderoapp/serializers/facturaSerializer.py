from parqueaderoapp.models.facturas import Factura
from rest_framework import serializers
class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = ['placa', 'costo_total', 'tipo_vehiculo', 'fecha_entrada', 'fecha_salida',]