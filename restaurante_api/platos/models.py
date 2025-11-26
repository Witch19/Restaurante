from django.db import models

class Plato(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True, null=True)
    categoria = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    disponible = models.BooleanField(default=True)
    tiempo_preparacion_min = models.IntegerField()
    calorias = models.IntegerField()
    es_vegetariano = models.BooleanField(default=False)
    
    NIVEL_PICANTE_CHOICES = [
        (0, 'Sin picante'),
        (1, 'Suave'),
        (2, 'Medio'),
        (3, 'Alto'),
    ]
    
    nivel_picante = models.IntegerField(choices=NIVEL_PICANTE_CHOICES, default=0)

    class Meta:
        ordering = ("nombre",)

    def __str__(self):
        return self.nombre
