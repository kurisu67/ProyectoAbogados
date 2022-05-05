from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, HttpResponse
from Holadjango.models import caso, demanda, informe2 
from .forms import informeform,demandaform, casoform
from django.shortcuts import render, redirect   
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
   if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('demandas')
        else : 
            return render(request, 'Holadjango/index.html', {"error": "Usuario no valido"})

   return render(request, 'Holadjango/index.html')




@login_required
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



def logout_view(request):
    logout(request)
    return redirect('index')

    
@login_required
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
    


@login_required
def casos(request):
    data = {
        'form' : casoform(),
        'user': request.user
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

@login_required
def listas_casos(request):
    listaas = caso.objects.filter(usuario=request.user.id)
    
    return render(request, 'Holadjango/listas_casos.html',{"listaas":listaas})

@login_required
def listas_demandas(request):
    listaas = demanda.objects.all()
    
    return render(request, 'Holadjango/listas_demandas.html',{"listaas":listaas})

@login_required
def listas_informes(request):
    listaas = informe2.objects.all()
    
    return render(request, 'Holadjango/listas_informes.html',{"listaas":listaas})


@login_required
def rest(request):
    return render(request, 'Holadjango/rest.html')

@login_required
def ultimademanda(request):
    return render(request, 'Holadjango/ultimademanda.html')

@login_required
def modificarcaso(request,id):
    reabrir = caso.objects.get(id_caso=id)
    data = {'form': casoform(instance=reabrir)}
    
    if request.method == 'POST':
        formulario = casoform(data=request.POST, instance=reabrir)
        if formulario.is_valid():
            formulario.save()
            return redirect('reabrircaso')
    
    return render(request, 'Holadjango/modificarcaso.html',data)

@login_required
def eliminarcaso(request,id):
    reabrir = caso.objects.get(id_caso=id)
    reabrir.delete()
    return redirect(to="reabrircaso")
    
@login_required
def reabrircaso(request):
    listaas = caso.objects.all()
    return render(request, 'Holadjango/reabrircaso.html',{"listaas":listaas})

@login_required
def reabrirdemanda(request):
    listaas = demanda.objects.all()
    return render(request, 'Holadjango/reabrirdemanda.html',{"listaas":listaas})

@login_required
def modificardemanda(request,id):
    reabrir = demanda.objects.get(id_demanda=id)
    data = {'form': demandaform(instance=reabrir)}
    
    if request.method == 'POST':
        formulario = demandaform(data=request.POST, instance=reabrir)
        if formulario.is_valid():
            formulario.save()
            return redirect('reabrirdemanda')
    
    return render(request, 'Holadjango/modificardemanda.html',data)

@login_required
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

@login_required
def reabririnforme(request):
    listaas = informe2.objects.all()
    return render(request, 'Holadjango/reabririnforme.html',{"listaas":listaas})

@login_required
def eliminarinforme(request,id):
    reabrir = informe2.objects.get(id_informe=id)
    reabrir.delete()
    return redirect(to="reabririnforme")

@login_required
def verdemanda(request,id):
    reabrir = demanda.objects.get(id_demanda=id)
    data = {'form': demandaform(instance=reabrir)}
          
    return render(request, 'Holadjango/verdemanda.html',data)

@login_required
def verinforme(request,id):
    reabrir = informe2.objects.get(id_informe=id)
    data = {'form': informeform(instance=reabrir)}
          
    return render(request, 'Holadjango/verinforme.html',data)

@login_required
def vercaso(request,id):
    reabrir = caso.objects.get(id_caso=id)
    data = {'form': casoform(instance=reabrir)}
          
    return render(request, 'Holadjango/vercaso.html',data)
    
    
    
   