from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, HttpResponse
from Holadjango.models import caso, demanda
from .forms import informeform,demandaform, nombreForm
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
    data ={
        'form' : demandaform()
    }
    if request.method=='POST':
        form = demandaform(data=request.POST)
        if form.is_valid():
            form.save()
            print("a")
            data ={
            'form' : form
            }
            return redirect('demanda')
        else:
            print("malo") 
            data["form"] = form
            return redirect('demandas')
    
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
    
    return render(request, 'Holadjango/casos.html')

def listas(request):
    return render(request, 'Holadjango/listas.html')

def rest(request):
    return render(request, 'Holadjango/rest.html')

def ultimademanda(request):
    return render(request, 'Holadjango/ultimademanda.html')


