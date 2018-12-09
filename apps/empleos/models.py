from django.db import models

class Empleado(models.Model):
	codigo_empleado = models.CharField(max_length = 20, primary_key = True)
	nombre_empleado = models.CharField(max_length= 50, null = False)
	fecha_nacimiento = models.DateField()
	tipo_empleado = models.CharField(max_length = 50, null = False)
	puntuacion = models.FloatField(default = 0.00)

# Create your models here.
