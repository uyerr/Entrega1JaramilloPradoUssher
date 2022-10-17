
import email
from unittest import loader
from django.http import HttpResponse
from django.template import Context, Template, loader
from django.shortcuts import render

from App1.models import User, Inicar
from App1.forms import UserForm, FindUserFormulario

def index(request):
    template = loader.get_template('Pagina_Blog/index.html')
    template_renderizado = template.render()
    return HttpResponse(template_renderizado)

def about(request):
    template = loader.get_template('Pagina_Blog/about.html')
    template_renderizado = template.render()
        
    return HttpResponse(template_renderizado)

def register(request):
    
    if request.method == 'POST':
        
        formulario = UserForm(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
        
            nombre = data['nombre']
            apellido = data['apellido']
            email = data['email']
            password = data['password']
            
            user = User(nombre=nombre, apellido=apellido, email=email, password=password)
            user.save()
            
            #return redirect('ver_personas')
    
    formulario = UserForm()
    
    return render(request, 'Pagina_Blog/register.html', {'formulario': formulario})

def user_list(request):
    
    nombre = request.GET.get('nombre')
    
    if nombre:
        usuarios = User.objects.filter(nombre__icontains=nombre)
    else:
        usuarios = User.objects.all()
        
    formulario = FindUserFormulario()
    
    return render(request, 'Pagina_Blog/user_list.html', {'usuarios': usuarios, 'formulario': formulario})

def iniciar_sesion(request):
    emails = Inicar.objects.all()
    paswords = Inicar.objects.all()
    return render(request, 'iniciar_sesion.html' )
    