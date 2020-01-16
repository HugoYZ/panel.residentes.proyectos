from django.urls import path

from . import views

app_name = 'banco_proyectos	'
urlpatterns = [

    path('', views.index, name='index'),
    path('base', views.base, name='base'),
    path('prueba', views.pruebas, name='pruebas'),
    path('registrar', views.registrar, name='registrar'),
    path('login', views.login, name='login'),
    path('agendarcita', views.agendarcita, name='agendarcita'),
    path('residentes', views.residentes, name='residentes'),
    path('archivosresidente', views.archivosresidente, name= 'archivosresidente'),


]