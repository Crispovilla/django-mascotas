from django.urls import path
from . import views

urlpatterns = [
    path('agregar/', views.agregar_veterinario, name='agregar_veterinario'),
    path('lista/', views.listar_veterinarios, name='lista_veterinarios'),
]