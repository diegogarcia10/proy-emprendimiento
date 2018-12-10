from django import forms
from apps.empleos.models import PerfilBuscado
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