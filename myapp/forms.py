from django import forms

class CreateNewProject (forms.Form):
    name = forms.CharField(label='Nombre del proyecto:', max_length=200)