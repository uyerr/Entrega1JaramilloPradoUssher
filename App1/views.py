
import email
from unittest import loader
from django.http import HttpResponse
from django.template import Context, Template, loader
from django.shortcuts import render

from App1.models import User, Inicar
from App1.forms import UserForm, FindUserFormulario

def index(request):
    template = loader.get_template('index.html')
    template_renderizado = template.render()
    return HttpResponse(template_renderizado)

def about(request):
    template = loader.get_template('about.html')
    template_renderizado = template.render()
        
    return HttpResponse(template_renderizado)


# def register(request):
#     template = loader.get_template('register.html')
#     template_renderizado = template.render()
        
#     return HttpResponse(template_renderizado)

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
    
    return render(request, 'register.html', {'formulario': formulario})
#def crear_usuario(request):
    #Crear(nombre = , apellido= ,email = ,passsword = ,)
    
    
    
    #return HttpResponse(' ')

def iniciar_sesion(request):
    emails = Inicar.objects.all()
    paswords = Inicar.objects.all()
    return render(request, 'iniciar_sesion.html' )
    