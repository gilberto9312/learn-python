from django import forms
from .models import Periodo

class PeriodoForm(forms.ModelForm):
    
    class Meta:
        model = Periodo
        fields = (
            "nombre",
            "fechaInicio",
            "fechaFin",
            "status",

            )
        labels = {
            "nombre": "Nombre",
            "fechaInicio": "Fecha de inicio",
            "fechaFin": "Fecha de fin",
            "status": "Estado",
 
        }
        widgets = {
            "nombre": forms.TextInput(attrs={'class':'form-control'}),
            "fechaInicio": forms.TextInput(attrs={'class':'form-control'}),
            "fechaFin": forms.TextInput(attrs={'class':'form-control'}),
            "status": forms.CheckboxInput(attrs={'class':'form-control'}),

        }
