from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,TemplateView


class vistaPerfil(TemplateView):
	template_name="perfil/perfil.html"
