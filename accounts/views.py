from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
from accounts.forms import UserCreate

def iniciar_sesion (request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            login(request, usuario) 
            return redirect('index')
    else:
        formulario = AuthenticationForm()    
        
        
    return render(request, 'accounts/login.html', {'formulario': formulario})

def register(request):
    if request.method == 'POST':
        formulario = UserCreate(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('index')
    else:
        formulario = UserCreate()
    
    return render(request, 'accounts/register.html', {'formulario': formulario})