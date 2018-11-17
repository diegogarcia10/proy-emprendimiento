from django.urls import path
from django.conf.urls import url,include
from django.contrib.auth.decorators import login_required
from apps.empleos.views import vistaPerfil, generarCurriculum

urlpatterns = [
	
	url(r'perfil', vistaPerfil.as_view(), name= 'perfil'),
	url(r'generarCurriculum', generarCurriculum, name = 'curriculum'),

]