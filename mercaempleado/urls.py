"""mercaempleado URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from django.contrib.auth.views import login, logout_then_login
from .views import home, index
from mercaempleado.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^index/', index, name='index'),
    url(r'^home/', home, name='home'),
    url(r'^empleado/',include('apps.empleos.urls')),
    url(r'^accounts/login/', login, {'template_name':'autentificacion/login.html'}, name='login'),
    url(r'^logout/',logout_then_login, name='logout'),

    url(r'^buscar/',busqueda, name='buscar-empleado'),

    url(r'^categorias/$',categorias,name="categorias"),

    url(r'^registrarse/$',RegistroUsuario.as_view(),name="registrarse"),
]
