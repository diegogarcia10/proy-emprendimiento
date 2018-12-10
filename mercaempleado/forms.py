from django import forms
from apps.empleos.models import PerfilBuscado, Publicacion
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):

	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
		]

		labels = {
			'username':'Nombre de usuario',
			'first_name':'Nombre',
			'last_name':'Apellidos',
			'email':'Email',

		}
	
class PerfilBuscadoForm(forms.ModelForm):

    class Meta:
        model = PerfilBuscado

        fields = [
            'nombre_perfil',
            'descripcion',

        ]
        labels = {
            'nombre_perfil' : 'Nombre de Perfil',
            'descripcion' : 'Descripcion',

        }

        widgets = {
            'nombre_perfil' : forms.TextInput(attrs={'class':'form-control'}),
            'descripcion' : forms.TextInput(attrs={'class':'form-control'}),

        }

class CrarPublicacionForm(forms.ModelForm):

    class Meta:
        model = Publicacion

        fields = [
        	'empleador',
            'titulo_publicacion',
            'requerimientos',
            'categoria',
            'perfil_buscado',
            'horarios_empleo',

        ]
        labels = {
        	'empleador': 'Nombre de Empleador',
            'titulo_publicacion' : 'Titulo de Publicacion',
            'requerimientos' : 'Requerimientos',
            'categoria' : 'Categotia',
            'perfil_buscado' : 'Perfil Buscado',
            'horarios_empleo' : 'Horario del Empleo',

        }

        widgets = {
        	'empleador': forms.Select(attrs={'class':'form-control'}),
            'titulo_publicacion' : forms.TextInput(attrs={'class':'form-control'}),
            'requerimientos' : forms.TextInput(attrs={'class':'form-control'}),
            'categoria' : forms.Select(attrs={'class':'form-control'}),
            'perfil_buscado' : forms.Select(attrs={'class':'form-control'}),
            'horarios_empleo' : forms.TextInput(attrs={'class':'form-control'}),

        }