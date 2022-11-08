from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
from accounts.forms import UserCreate, ProfileEditForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from accounts.models import ExtensionUsuario

def iniciar_sesion (request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        
        if formulario.is_valid():
            user = formulario.get_user()
            login(request, user) 
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


@login_required
def profile(request):
    
    extensionUsuario, es_nuevo = ExtensionUsuario.objects.get_or_create(user=request.user)
    
    return render(request, 'accounts/profile.html', {})


@login_required
def edit_profile(request):
    
    user = request.user
    
    if request.method == 'POST':
       formulario = ProfileEditForm(request.POST, request.FILES)
       
       if formulario.is_valid():
           data = formulario.cleaned_data
           
           user.first_name = data['first_name']
           user.last_name = data['last_name']
           user.email = data['email']
           user.extensionusuario.description = data['description']
           user.extensionusuario.website = data['website']
           user.extensionusuario.avatar = data['avatar']
           
           user.save()
           user.extensionusuario.save()
           
           return redirect('profile')
    else:   
        formulario = ProfileEditForm(
            initial={
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'description': user.extensionusuario.description,
                'website': user.extensionusuario.website,
                'avatar': user.extensionusuario.avatar,
            }
        )
    
    return render(request, 'accounts/edit_profile.html', {'formulario': formulario})


class password(LoginRequiredMixin, PasswordChangeView):
    
    template_name = 'accounts/password.html'
    success_url = '/accounts/profile/'