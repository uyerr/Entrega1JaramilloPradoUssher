import email
from unicodedata import name
from django import forms


class FindUserFormulario(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)