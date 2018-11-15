from django.shortcuts import render



def home(request):
	return render(request,'home/home.html')

def index(request):
	return render(request,'base/base.html')

def categorias(request):
	return render(request,'categorias/categorias.html')	