from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, HttpResponse
from Holadjango.models import caso, demanda, informe2 
from .forms import informeform,demandaform, nombreForm, casoform
from django.shortcuts import render, redirect   

 


# Create your views here.
def index(request):
    return render(request, 'Holadjango/index.html')
def get_nombre(request):
    form = nombreForm(request.POST)
    if request.method=='POST':
        if form.is_valid():
            return render(request, 'Holadjango/index.html')
        else:
            form= nombreForm()
    return render(request , 'Holadjango/nombre.html', {'form': form})


def demandas(request):
    data = {
        'form' : demandaform()
    }
    
    if request.method == 'POST':
        formulario = demandaform(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]= "informe guardado"
            return redirect('demandas')
        else:
            data["form"] = formulario
            return redirect ('demandas')
    
    
    return render(request, 'Holadjango/demandas.html',data)
    

def informe(request):
    data = {
        'form' : informeform()
    }

    if request.method == 'POST':
       formulario = informeform(data=request.POST)
       if formulario.is_valid():
           formulario.save()
           data["mensaje"]= "informe guardado"
           return redirect('informe')
       else:
           data["form"] = formulario
           return redirect('informe')

    return render(request, 'Holadjango/informe.html',data)
    



def casos(request):
    data = {
        'form' : casoform()
    }
    if request.method == 'POST':
        formulario= casoform(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]= "informe guardado"
            return redirect('casos')
        else:
            data["form"] = formulario
            return redirect('casos')
    
    return render(request, 'Holadjango/casos.html',data)

def listas_casos(request):
    listaas = caso.objects.all()
    
    return render(request, 'Holadjango/listas_casos.html',{"listaas":listaas})

def listas_demandas(request):
    listaas = demanda.objects.all()
    
    return render(request, 'Holadjango/listas_demandas.html',{"listaas":listaas})

def listas_informes(request):
    listaas = informe2.objects.all()
    
    return render(request, 'Holadjango/listas_informes.html',{"listaas":listaas})



def rest(request):
    return render(request, 'Holadjango/rest.html')

def ultimademanda(request):
    return render(request, 'Holadjango/ultimademanda.html')

def modificarcaso(request,id):
    reabrir = caso.objects.get(id_caso=id)
    data = {'form': casoform(instance=reabrir)}
    
    if request.method == 'POST':
        formulario = casoform(data=request.POST, instance=reabrir)
        if formulario.is_valid():
            formulario.save()
            return redirect('reabrircaso')
    
    return render(request, 'Holadjango/modificarcaso.html',data)

def eliminarcaso(request,id):
    reabrir = caso.objects.get(id_caso=id)
    reabrir.delete()
    return redirect(to="reabrircaso")
    

def reabrircaso(request):
    listaas = caso.objects.all()
    return render(request, 'Holadjango/reabrircaso.html',{"listaas":listaas})

def reabrirdemanda(request):
    listaas = demanda.objects.all()
    return render(request, 'Holadjango/reabrirdemanda.html',{"listaas":listaas})

def modificardemanda(request,id):
    reabrir = demanda.objects.get(id_demanda=id)
    data = {'form': demandaform(instance=reabrir)}
    
    if request.method == 'POST':
        formulario = demandaform(data=request.POST, instance=reabrir)
        if formulario.is_valid():
            formulario.save()
            return redirect('reabrirdemanda')
    
    return render(request, 'Holadjango/modificardemanda.html',data)

def eliminardemanda(request,id):
    reabrir = demanda.objects.get(id_demanda=id)
    reabrir.delete()
    return redirect(to="reabrirdemanda")

def modificarinforme(request,id):
    reabrir = informe2.objects.get(id_informe=id)
    data = {'form': informeform(instance=reabrir)}
    
    if request.method == 'POST':
        formulario = informeform(data=request.POST, instance=reabrir)
        if formulario.is_valid():
            formulario.save()
            return redirect('reabrirdemanda')
    
    return render(request, 'Holadjango/modificarinforme.html',data)

def reabririnforme(request):
    listaas = informe2.objects.all()
    return render(request, 'Holadjango/reabririnforme.html',{"listaas":listaas})

def eliminarinforme(request,id):
    reabrir = informe2.objects.get(id_informe=id)
    reabrir.delete()
    return redirect(to="reabririnforme")