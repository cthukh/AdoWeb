from django import forms
from .models import Holomem 

class HolomemForm(forms.ModelForm):
    class Meta:
        model = Holomem
        fields = [
            'nombre',
            'descripcion',
            'cant_seguidores',
            'fecha_debut',
            'activo',
            'generacion',
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                #'placeholder': 'Ej: Don Quijote de la Mancha',
            }),
            'descripcion': forms.TextInput(attrs={
                'class': 'form-control', 
            }),
            'cant_seguidores': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cantidad de seguidores en YouTube'
            }),
            'fecha_debut': forms.DateInput(attrs={
                'class': 'form-control',
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
            'generacion': forms.Select(attrs={
                'class': 'form-select',
            })
        }