from django.db import models

class Categoria(models.Model):
	nombre_categoria = models.CharField(max_length = 50)
	descripcion = models.CharField(max_length = 200)
	def __str__(self): 
    		return self.nombre_categoria
	class Meta:
        	ordering = ['nombre_categoria']

class Empleado(models.Model):
	codigo_empleado = models.CharField(max_length = 20, primary_key = True)
	nombre_empleado = models.CharField(max_length= 50, null = False)
	apellidos_empleado = models.CharField(max_length = 50)
	fecha_nacimiento = models.DateField()
	tipo_empleado = models.CharField(max_length = 50, null = False)
	puntuacion = models.FloatField(default = 0.00)
	email = models.CharField(max_length = 25, null = True)
	telefono = models.CharField(max_length = 9, null = True)
	direccion = models.CharField(max_length = 80, null = True)
	descripcion=models.CharField(max_length=150,null=True)


class Curriculum(models.Model):
	empleado = models.ForeignKey(Empleado, on_delete = models.CASCADE)
	objetivo = models.CharField(max_length = 150, null = True)

class Habilidad(models.Model):
	curriculum = models.ForeignKey(Curriculum, on_delete = models.CASCADE)
	habilidad = models.CharField(max_length = 50)
	grado_desarrollo = models.FloatField()

class PreparacionAcademica(models.Model):
	curriculum = models.ForeignKey(Curriculum, on_delete = models.CASCADE)
	institucion = models.CharField(max_length = 50)
	grado_academico = models.CharField(max_length = 50)
	especializacion = models.CharField(max_length = 50)

class ExperienciaLaboral(models.Model):
	curriculum = models.ForeignKey(Curriculum, on_delete = models.CASCADE)
	empresa = models.CharField(max_length = 50)
	ubicacion_empresa = models.CharField(max_length = 100)
	puesto_ejercido = models.CharField(max_length = 50)
	tareas_realizadas = models.CharField(max_length = 150)
	fecha_entrada = models.DateField()
	fecha_salida = models.DateField()
	razon_salida = models.CharField(max_length = 150)

class Empleador(models.Model):
	codigo_empleador = models.CharField(max_length = 50, primary_key = True)
	nombre_comercial = models.CharField(max_length = 50)
	tipo_empleador = models.CharField(max_length = 25)
	puntuacion = models.FloatField(default = 0.00)
	direccion = models.CharField(max_length = 150)
	telefono = models.CharField(max_length = 9)
	email = models.CharField(max_length = 50)

class Contrato(models.Model):
	empleador = models.ForeignKey(Empleador, on_delete = models.CASCADE)
	empleado = models.ForeignKey(Empleado, on_delete = models.CASCADE)
	fecha_contrato = models.DateField()
	descripcion_empleador = models.CharField(max_length = 200)
	acuerdos = models.CharField(max_length = 150)
	restricciones = models.CharField(max_length = 150)
	sueldo_nominal = models.FloatField()
	temporada = models.BooleanField()

class Referencias(models.Model):
	contrato = models.ForeignKey(Contrato, on_delete = models.CASCADE)
	puntuacion_empleado = models.FloatField()
	referencia_empleado = models.CharField(max_length = 200, null = True)
	puntuacion_empleador = models.FloatField()
	referencia_empleador = models.CharField(max_length = 200, null = True)



class PerfilBuscado(models.Model):
	nombre_perfil = models.CharField(max_length = 150)
	descripcion = models.CharField(max_length = 200)

class Publicacion(models.Model):
	empleador = models.ForeignKey(Empleador, on_delete = models.CASCADE)
	titulo_publicacion = models.CharField(max_length = 100)
	requerimientos = models.CharField(max_length = 350)
	categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
	perfil_buscado = models.ForeignKey(PerfilBuscado, on_delete = models.CASCADE)
	horarios_empleo = models.CharField(max_length = 150)

class Prueba(models.Model):
	publicacion = models.ForeignKey(Publicacion, on_delete = models.CASCADE)
	descripcion = models.CharField(max_length = 200)
	fecha_creacion = models.DateField()
	fecha_programada = models.DateField()
	hora_programada = models.CharField(max_length = 10)
	temas_evaluar = models.CharField(max_length = 200)

class Pregunta(models.Model):
	prueba = models.ForeignKey(Prueba, on_delete = models.CASCADE)
	opciones = models.CharField(max_length = 150)
	respuesta_correcta = models.CharField(max_length = 100)
	porcentaje = models.FloatField()

class Interesado(models.Model):
	publicacion = models.ForeignKey(Publicacion, on_delete = models.CASCADE)
	empleado = models.ForeignKey(Empleado, on_delete = models.CASCADE)
	aceptado = models.BooleanField()

class Respuesta(models.Model):
	interesado = models.ForeignKey(Interesado, on_delete = models.CASCADE)
	pregunta = models.ForeignKey(Pregunta, on_delete = models.CASCADE)
	opcion_seleccionada = models.CharField(max_length = 150)
	porcentaje_obtenido = models.FloatField()