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
	return render(request, 'perfil/generarCurriculum.html')

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

def categorias(request, cat='1'):
	categoria = Categoria.objects.all()
	existe = Publicacion.objects.filter(categoria_id = cat).exists()
	if existe:
		pub= Publicacion.objects.filter(categoria_id = cat)
	else:
		pub = ''

	contexto={'categorias':categoria,'pub':pub}
	return	render(request, 'categorias/categorias.html',contexto)
		