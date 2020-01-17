from django.shortcuts import render
from django.http import HttpResponse



def bienvenido(request):
	return render(request, 'paginas/bienvenido.html')

def vistaprincipal(request):
	return render(request, 'paginas/vistaprincipal.html')


def login(request):
	return render(request, 'paginas/login.html')

def registrar(request):
	return render(request, 'paginas/registrar.html')


def agendar(request):
	return render(request, 'paginas/agendar.html')

def residentes(request):
	return render(request, 'paginas/residentes.html')

def archivosr(request):
	return render(request, 'paginas/archivosr.html')

def restablecercontraseña(request):
	return render(request, 'paginas/restablecercontraseña.html')

def verproyectos(request):
	return render(request, 'paginas/verproyectos.html')