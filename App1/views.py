
from unittest import loader
from django.http import HttpResponse
from django.template import Context, Template, loader
from django.shortcuts import render

from App1.models import Crear, Inicar

def home(request):
    template = loader.get_template('index.html')
    template_renderizado = template.render()
    return HttpResponse(template_renderizado)

#def crear_usuario(request):
    #Crear(nombre = , apellido= ,email = ,passsword = ,)
    
    
    
    #return HttpResponse(' ')

def iniciar_sesion(request):
    emails = Inicar.objects.all()
    paswords = Inicar.objects.all()
    return render(request, 'iniciar_sesion.html' )
    