from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import RegistroForm


def home(request):
	return render(request,'home/home.html')

def index(request):
	return render(request,'base/base.html')


def busqueda(request):
	return render(request,'busquedaTrabajador/busqtrabajador.html')

def categorias(request):
	return render(request,'categorias/categorias.html')	

class RegistroUsuario(CreateView):
	model = User
	template_name = 'autentificacion/registrar.html'
	form_class = RegistroForm
	success_url = reverse_lazy('login')	

