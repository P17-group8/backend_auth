from parqueaderoapp.models.plazas import Plazas
from rest_framework import serializers
class PlazasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plazas
        fields = ['tipo_plaza', 'codigo_plaza', 'estado']