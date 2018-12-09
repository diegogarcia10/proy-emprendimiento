from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from apps.empleos.models import *
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