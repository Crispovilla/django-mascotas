from django.shortcuts import render, redirect
from .forms import VeterinarioForm
from .models import Veterinario

# Create your views here.
def agregar_veterinario(request):
    if request.method == 'POST':
        form = VeterinarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_veterinarios')
    else:
        form = VeterinarioForm()
    return render(request, 'veterinarios/agregar_veterinario.html', {'form': form})

def listar_veterinarios(request):
    veterinarios = Veterinario.objects.all()

    return render(request, 'veterinarios/lista_veterinarios.html', {'veterinarios': veterinarios})