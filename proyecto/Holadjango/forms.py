from django import forms
from .models import informe, caso, demanda


class informeform(forms.ModelForm):

    class Meta:
        model = informe 
        fields =["descripcion"]


class casoform(forms.ModelForm):
    class Meta:
        model = caso
        fields =[ "cantidad_demandas","descripcion"]
        

class demandaform(forms.Form):
    nombre_tipo = forms.CharField(max_length=200)
    Descripcion = forms.CharField(max_length=1000)
    rut=forms.CharField(max_length=10)
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    telefono=forms.CharField(max_length=12)
    comuna=forms.CharField(max_length=50)
    region=forms.CharField(max_length=50)
    rutdemando=forms.CharField(max_length=10)
    nombredemando=forms.CharField(max_length=50)
    apellidodemando=forms.CharField(max_length=50)
    telefonodemando=forms.CharField(max_length=12)
    comunademando=forms.CharField(max_length=50)
    regiondemando=forms.CharField(max_length=50)
    
    def clean_demanda(self):
        cleaned_data = self.cleaned_data
        demanda = cleaned_data.get('demanda')
        return demanda
    
    
    
    class Meta:
        model = demanda
        fields = [
            "nombre_tipo",
            "Descripcion",
            "rut",
            "nombre",
            "apellido",
            "telefono",
            "comuna",
            "region",
            "rutdemando",
            "nombredemando",
            "apellidodemando",
            "telefonodemando",
            "comunademando",
            "regiondemando"]
        
class nombreForm(forms.Form):
    nombre = forms.CharField (label="Nombre: ", max_length=100)
    apellido = forms.CharField (label="apellido: ", max_length=100)
