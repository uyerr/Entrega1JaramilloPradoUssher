
import email
from unittest import loader
from django.http import HttpResponse
from django.template import Context, Template, loader
from django.shortcuts import render

from App1.models import User, Inicar
from App1.forms import FindUserFormulario

def index(request):
    template = loader.get_template('Pagina_Blog/index.html')
    template_renderizado = template.render()
    return HttpResponse(template_renderizado)

def about(request):
    template = loader.get_template('Pagina_Blog/about.html')
    template_renderizado = template.render()
        
    return HttpResponse(template_renderizado)

def user_list(request):
    
    nombre = request.GET.get('nombre')
    
    if nombre:
        usuarios = User.objects.filter(nombre__icontains=nombre)
    else:
        usuarios = User.objects.all()
        
    formulario = FindUserFormulario()
    
    return render(request, 'Pagina_Blog/user_list.html', {'usuarios': usuarios, 'formulario': formulario})


    