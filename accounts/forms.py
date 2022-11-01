from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
class UserCreate(UserCreationForm):
    
    my_name = forms.CharField(label = 'Name', max_length=30)
    email = forms.EmailField(label = 'Email', max_length=30)
    password1 = forms.CharField(label = 'Password',widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Repeat Password', widget = forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['my_name','email', 'password1', 'password2']
        help_text = {key: '' for key in fields}