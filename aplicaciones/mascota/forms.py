from django import forms
from aplicaciones.mascota.models import Mascota


Class MascotaForm(forms.ModelForm):
    
    class Meta:
        model=Mascota

        fields= [
            'adoptante',
            'tipo',
            'nombre',
            'sexo',
            'edad',
            'raza',
            'foto',
            'adoptado',
        ] 

        labels={
            'adoptante':'Adoptante',
            'tipo':'Tipo',
            'nombre':'Nombre',
            'sexo':'Sexo',
            'edad':'Edad',
            'raza':'Raza',
            'foto':'Foto',
            'adoptado':'Adoptado',
        }
        widgets={
            'adoptante':forms.select(attrs={'class':'form-control'}),
            'tipo':forms.select(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'sexo':forms.TextInput(attrs={'class':'form-control'}),
            'edad':forms.TextInput(attrs={'class':'form-control'}),
            'raza':forms.TextInput(attrs={'class':'form-control'}),
            'foto':forms.TextInput(attrs={'class':'form-control'}),
            'adoptado':forms.CheckboxSelectMultiple(),
        }