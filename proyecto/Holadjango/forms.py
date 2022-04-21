from django import forms
from .models import informe2, caso, demanda


class informeform(forms.ModelForm):

    class Meta:
        model = informe2
        fields =["titulo","descripcion"]


class casoform(forms.ModelForm):
    class Meta:
        model = caso
        fields =[ "cantidad_demandas","titulo","descripcion"]
        

class demandaform(forms.ModelForm):
    ##Descripcion = forms.CharField(widget=forms.TextInput(attrs={'class':''}))
    class Meta:
        model = demanda
        fields = [
            "nombre_tipo",
            "titulo",
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
