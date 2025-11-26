from rest_framework import serializers
from .models import Plato

class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plato
        fields = (
            "id",
            "codigo",
            "nombre",
            "descripcion",
            "categoria",
            "precio",
            "disponible",
            "tiempo_preparacion_min",
            "calorias",
            "es_vegetariano",
            "nivel_picante"
        )
        read_only_fields = ("id", "codigo")


def validate_precio(self, value):
    if value <= 0:
        raise serializers.ValidationError("El precio debe ser mayor a 0.")
    return value

