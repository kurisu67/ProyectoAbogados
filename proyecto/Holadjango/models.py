from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class caso(models.Model):
     
    id_caso=models.BigAutoField(primary_key=True)
    titulo=models.CharField(max_length=20)
    descripcion=models.CharField(max_length=1000)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    usuario=models.ForeignKey(User, on_delete=models.CASCADE)
    

    class Meta:
        verbose_name= 'caso'
        verbose_name_plural= 'casos'

        
    def __str__(self):
        return str(self.titulo)    


class demanda(models.Model):
    id_demanda=models.BigAutoField(primary_key=True)
    titulo=models.CharField(max_length=20)
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
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    id_caso=models.ForeignKey(caso, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name= 'demanda'
        verbose_name_plural= 'demandas'

        
    def __str__(self):
        return str(self.titulo)


class informe2(models.Model):
    id_informe=models.BigAutoField(primary_key=True)
    titulo=models.CharField(max_length=20)
    descripcion=models.CharField(max_length=1000)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    id_demanda=models.ForeignKey(demanda, on_delete=models.CASCADE)
    class Meta:
        verbose_name= 'informe2'
        verbose_name_plural= 'informes2'

        
    def __str__(self):
        return str(self.id_informe)
