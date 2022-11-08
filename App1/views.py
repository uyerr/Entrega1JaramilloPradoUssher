
import email
from unittest import loader
from django.http import HttpResponse
from django.template import Context, Template, loader
from django.shortcuts import render

from App1.models import User, Inicar
from App1.forms import FindUserFormulario

def index(request):
    
    return render(request, 'Pagina_Blog/index.html')

def about(request):
    
    return render(request, 'Pagina_Blog/about.html')

def user_list(request):
    
    nombre = request.GET.get('nombre')
    
    if nombre:
        usuarios = User.objects.filter(nombre__icontains=nombre)
    else:
        usuarios = User.objects.all()
        
    formulario = FindUserFormulario()
    
    return render(request, 'Pagina_Blog/user_list.html', {'usuarios': usuarios, 'formulario': formulario})


    