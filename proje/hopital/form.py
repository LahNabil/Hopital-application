from django import forms
from .models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['nom','date_Naissance','malade']
        widgets = {
            'nom': forms.TextInput(attrs={'class':'form-control'}),
            'date_Naissance': forms.TextInput(attrs={'class':'form-control'})
        }