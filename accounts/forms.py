from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class UserCreate(UserCreationForm):
    
    username = forms.CharField(label = 'Username', max_length=30)
    email = forms.EmailField(label = 'Email', max_length=30)
    password1 = forms.CharField(label = 'Password',widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Repeat Password', widget = forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
        help_text = {key: '' for key in fields}
        
class ProfileEditForm(forms.Form):
    
    first_name = forms.CharField(label='Nombre', required=False)
    last_name = forms.CharField(label='Apellido', required=False)
    email = forms.CharField(required=False)
    description = forms.CharField(label='descripcion', required=False)
    website = forms.URLField(label='website', required=False)
    avatar = forms.ImageField(required=False, )
    
class UserFindForm(forms.Form):
    username = forms.CharField(max_length=30, required=False, label='')