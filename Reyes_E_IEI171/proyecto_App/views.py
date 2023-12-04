from django.shortcuts import redirect, render
from proyecto_App.models import Club

from .forms import FormProyecto


def index(request):
    return render(request, 'index.html')

def listadosocio(request):                                                 
    proye = Club.objects.all()
    data = {'proyec':proye}
    return render(request, 'listado.html', data)

def agregarsocio(request):
    if request.method == 'POST':
        form = FormProyecto(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listado')
    else:
        form = FormProyecto()

    data = {'form': form}
    return render(request, 'agregar.html', data)

def modificarsocio(request , id):

    pro = Club.objects.get(id = id)
    form = FormProyecto(instance=pro)

    if (request.method == "POST"):
        form = FormProyecto(request.POST, instance=pro)
        if(form.is_valid()):
            form.save()
            return redirect('/listado')
  
    data = {'form' :form }
    return render(request, 'agregar.html', data)

def eliminarsocio(request, id):
    pro = Club.objects.get(id = id)
    pro.delete()
    return redirect('/listado')