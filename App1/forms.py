import email
from unicodedata import name
from django import forms

class UserForm(forms.Form):
    name = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    email = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)
    
    
class FindUserFormulario(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)