from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from apps.empleos.models import *
from django.core import serializers
from django.http import HttpResponse
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,TemplateView


class vistaPerfil(TemplateView):
	template_name="perfil/perfil.html"

def generarCurriculum(request):
	empleado = Empleado.objects.get(usuario_empleado__username = request.user)
	curriculum_e = Curriculum.objects.filter(empleado = empleado).exists()
	if curriculum_e:
		curriculum = Curriculum.objects.get(empleado = empleado)
		pass
	else:
		curriculum = False

	if 'btnGuardarCurriculum' in request.POST:
		empleado = Empleado.objects.get(usuario_empleado__username = request.user)
		objetivo = request.POST['txtObjetivo']
		curriculum = Curriculum(empleado = empleado, objetivo = objetivo)
		curriculum.save()
		pass

	if 'btnGuardarExp' in request.POST:
		curriculum_id = request.POST['curriculumExp']
		curriculum = Curriculum.objects.get(id = curriculum_id)
		empresa = request.POST['txtEmpresa']
		ubicacion_empresa = request.POST['txtUbicacion']
		puesto_ejercido = request.POST['txtPuesto']
		tareas_realizadas = request.POST['txtTareas']
		fecha_entrada = request.POST['txtFechaEntrada']
		fecha_salida = request.POST['txtFechaSalida']
		razon_salida = request.POST['txtRazonSalida']
		exp = ExperienciaLaboral(curriculum = curriculum, empresa = empresa, ubicacion_empresa = ubicacion_empresa, puesto_ejercido = puesto_ejercido, tareas_realizadas = tareas_realizadas, fecha_entrada = fecha_entrada, fecha_salida = fecha_salida, razon_salida = razon_salida)
		exp.save()
		pass

	if 'btnGuardarEdu' in request.POST:
		curriculum_id = request.POST['curriculumEdu']
		curriculum = Curriculum.objects.get(id = curriculum_id)
		institucion = request.POST['txtInstitucion']
		grado_academico = request.POST['txtGradoAcademico']
		especializacion = request.POST['txtEspecializacion']
		edu = PreparacionAcademica(curriculum = curriculum, institucion = institucion, grado_academico = grado_academico, especializacion = especializacion)
		edu.save()
		pass

	if 'btnGuardarHab' in request.POST:
		curriculum_id = request.POST['curriculumHab']
		curriculum = Curriculum.objects.get(id = curriculum_id)
		habilidad = request.POST['txtHabilidad']
		grado_desarrollo = float(request.POST['txtGradoDesarrollo'])
		hab = Habilidad(curriculum = curriculum, habilidad = habilidad, grado_desarrollo = grado_desarrollo)
		hab.save()
		pass

	contexto = {'curriculum':curriculum, 'empleado':empleado}
	return render(request, 'perfil/generarCurriculum.html',contexto)

def verCurriculum(request):
	empleado = Empleado.objects.get(usuario_empleado__username = request.user)
	curriculum_e = Curriculum.objects.filter(empleado = empleado).exists()
	if curriculum_e:
		curriculum = Curriculum.objects.get(empleado = empleado)
		experiencias = ExperienciaLaboral.objects.filter(curriculum = curriculum)
		educaciones = PreparacionAcademica.objects.filter(curriculum = curriculum)
		habilidades = Habilidad.objects.filter(curriculum = curriculum)
		pass
	else:
		curriculum = False
		experiencias = False
		educaciones = False
		habilidades = False

	contexto = {'empleado':empleado, 'curriculum':curriculum, 'experiencias':experiencias, 'educaciones':educaciones, 'habilidades':habilidades }
	return render(request, 'perfil/verCurriculum.html', contexto)


class crearPublicacion(TemplateView):
	template_name="publicacion/crearPublicacion.html"

def busqueda(request):
	emple=Empleado.objects.all()
	categoria=Categoria.objects.all()
	contexto={'empleados':emple,'categorias':categoria}
	return render(request,'busquedaTrabajador/busqtrabajador.html',contexto)


def busquedaAjaxView(request):
	emples=Empleado.objects.filter(categoria=request.GET['id'])
	data=serializers.serialize('json',emples,
		fields=('nombre_empleado','apellidos_empleado','descripcion','telefono'))
	return HttpResponse(data,content_type='application/json')


class vistaAcercaDeNosotros(TemplateView):
	template_name="AcercaDeNosotros/AcercaDeNosotros.html"

		

def ListaPublicaciones(request):
	lista=Publicacion.objects.all()
	contexto={'lp':lista}
	return render(request,'publicacion/lista-p.html',contexto)

def Prueba(request):

	return render(request,'publicacion/prueba.html')


def categorias(request, cat='1'):
	categoria = Categoria.objects.all()
	existe = Publicacion.objects.filter(categoria_id = cat).exists()
	if existe:
		pub= Publicacion.objects.filter(categoria_id = cat)
	else:
		pub = ''

	contexto={'categorias':categoria,'pub':pub}
	return	render(request, 'categorias/categorias.html',contexto)
		

