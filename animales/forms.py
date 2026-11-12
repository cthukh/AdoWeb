from django import forms
from .models import Animal

class AnimalForm(forms.Modelform):
    class Meta:
        model = Animal
        fields = [
            'nombre',
            'edad',
            'descripcion',
            'fecha_ingreso',
            'especie',
            'disponible',
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del animal',
            }),
            'edad': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Edad del animal',
                'min': '0',
            }),
            'descripcion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Puedes agregar una descripción del animal',
            }),
            'fecha_ingreso': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'especie': forms.Select(attrs={
                'class': 'form-select',
            }),
            'disponible': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }