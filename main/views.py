from django.shortcuts import render, HttpResponse

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