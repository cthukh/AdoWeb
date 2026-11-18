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
                'placeholder': 'Ej: Hoshimachi Suisei',
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Una breve descripción del talento',
            }),
            'cant_seguidores': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cantidad de seguidores en YouTube Ej: 2.930.000',
                'min': '0',
            }),
            'fecha_debut': forms.DateInput(format='%Y-%m-%d', attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
            'generacion': forms.Select(attrs={
                'class': 'form-select',
            }),
        }