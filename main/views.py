from django.shortcuts import render,redirect, HttpResponse
from .forms import MascotaForm
from .models import Mascota
# Create your views here.

def bienvenida(request):
    return render(request, 'main/bienvenida.html')

def mascotas(request):
    mascotas = ['Perrito', 'Gatito', 'Hamstercito']
    
    return render(request, 'mascotas/mascotas.html', {'mascotas': mascotas})

def saludo(request, nombre):
    return HttpResponse(f"¡Hola, {nombre}")

def detalle_mascota(request, mascota):
    detalle_mascota={
        'Perrito': 'Este es muy jugueton'
    } 
    return render(request, 'mascotas/detalle_mascota.html', {'mascota':mascota})

def agregar_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_mascotas')
    else:
        form = MascotaForm()
    return render(request, 'main/agregar_mascota.html', {'form': form})

def lista_mascotas(request):
    mascotas = Mascota.objects.all()

    return render(request, 'main/lista_mascotas.html', {'mascotas': mascotas})