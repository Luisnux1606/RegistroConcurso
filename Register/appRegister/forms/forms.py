from django import forms
from ..models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        fields = ['cedula','nombres','apellidos','nro_fono','carrera','edad','mail','estado']
        model = Persona
