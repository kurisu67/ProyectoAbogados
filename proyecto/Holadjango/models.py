from django.db import models
# Create your models here.
region=[
    (1,"Región de tarapacá"),
    (2,"Region pete")
]
tipo= [
    (1, "Primer tipo"),
    (2, "Segundo tipo"),
    (3, "Tercer tipo")
]
class informe(models.Model):
    id_informe=models.BigAutoField(primary_key=True) 
    descripcion=models.CharField(max_length=1000)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name= 'informe'
        verbose_name_plural= 'informes'

        
    def __str__(self):
        return str(self.id_informe)

class caso(models.Model):
    id_caso=models.BigAutoField(primary_key=True)
    cantidad_demandas=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=1000)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name= 'caso'
        verbose_name_plural= 'casos'

        
    def __str__(self):
        return str(self.id_caso)
    ##tipo de demanda


class demanda(models.Model):
    id_demanda=models.AutoField(primary_key=True)
    nombre_tipo=models.CharField(max_length=200)
    Descripcion=models.CharField(max_length=1000,default="")
    rut=models.CharField(max_length=10,default="")
    nombre=models.CharField(max_length=50,default="")
    apellido=models.CharField(max_length=50,default="")
    telefono=models.CharField(max_length=12,default="")
    comuna=models.CharField(max_length=50,default="")
    region=models.CharField(max_length=50)
    rutdemando=models.CharField(max_length=10,default="")
    nombredemando=models.CharField(max_length=50,default="")
    apellidodemando=models.CharField(max_length=50,default="")
    telefonodemando=models.CharField(max_length=12,default="")
    comunademando=models.CharField(max_length=50,default="")
    regiondemando=models.CharField(max_length=50)
   

    
    class Meta:
        verbose_name= 'demanda'
        verbose_name_plural= 'demandas'

        
    def __str__(self):
        return str(self.id_demanda)



class nombre (models.Model):
    nombre= models.CharField(max_length=100)
    def __str__(self):
        return str(self.nombre)