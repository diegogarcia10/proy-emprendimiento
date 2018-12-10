from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from apps.empleos.models import *
from .forms import RegistroForm
from mercaempleado.forms import PerfilBuscadoForm, CrarPublicacionForm


def home(request):
	return render(request,'home/home.html')

def index(request):
	return render(request,'base/base.html')


def categorias(request):
	return render(request,'categorias/categorias.html')	


class RegistroUsuario(CreateView):
	model = User
	template_name = 'autentificacion/registrar.html'
	form_class = RegistroForm
	success_url = reverse_lazy('login')	

class PerfilBuscadoCreate(CreateView):
	model = PerfilBuscado
	form_class = PerfilBuscadoForm
	template_name = 'Publicacion/PerfilBuscado.html'
	success_url = reverse_lazy('crearPublicacion')

def crearPublicacion(request):
	if request.method=='POST':
		form = CrarPublicacionForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('lista')
	else:
		form = CrarPublicacionForm()

	return render(request, 'publicacion/crearPublicacion.html', {'form':form})
	#si el metodo es POST Hacer esto
#	if request.method=='POST':
		#Resivimos todos los parametros del formulario
#		form1=CrarPublicacionForm(request.POST)
		#si el formulario es Valido hacer lo siguiente 
#		if form1.is_valid():
			#Hacemos la creacion de los objetos 
			#publicacion=Publicacion()
			#_userid = request.user.id
			#id_empleador = User.objects.get(id=_userid)
			#Asignammos a cada objeto lo que resivimos de cada campo del formulario
#			publicacion.empleador=request.POST['empleador']
#			publicacion.titulo_publicacion=request.POST['titulo_publicacion']
#			publicacion.requerimientos=request.POST['requerimientos']
#			publicacion.categoria=request.POST['categoria']
#			publicacion.perfil_buscado=request.POST['perfil_buscado']
#			publicacion.horarios_empleo=request.POST['horarios_empleo']
			
	
			#Guardamos  
#			publicacion.save()	
#							
#		return redirect('lista')
#	else:
		#muestra el formulario
#		form1=CrarPublicacionForm()
#		contexto={'form1':form1}		
#	return render(request,'publicacion/crearPublicacion.html',contexto)