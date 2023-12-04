from django import forms
from .models import Club

class FormProyecto(forms.ModelForm):
    class Meta:
        model = Club
        fields = '__all__'