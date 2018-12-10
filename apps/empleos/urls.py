from django.urls import path
from django.conf.urls import url,include
from django.contrib.auth.decorators import login_required
from apps.empleos.views import *

urlpatterns = [
	
	url(r'perfil', vistaPerfil.as_view(), name= 'perfil'),
	url(r'generarCurriculum', generarCurriculum, name = 'curriculum'),
	url(r'crearPublicacion', crearPublicacion.as_view(), name= 'crearPublicacion'),
    url(r'^buscar/',busqueda, name='buscar-empleado'),
    url(r'^acercade',vistaAcercaDeNosotros.as_view(),name="acercadenosotros"),

    

    
    path('',categorias, name= "categoria"),  
    url(r'^(?P<cat>\d+)/$',categorias,name="categoria1"),
    

	url(r'^busq/$', busquedaAjaxView,name='busq'),

]