from django.urls import path
from . import views

urlpatterns = [
    path('bienvenida/', views.bienvenida, name='bienvenida'),
    path('mascotas/', views.mascotas, name='mascotas'),
    path('mascotas/detalle_mascota/<str:mascota>/', views.detalle_mascota, name='detalle_mascota'),
    path('agregar/', views.agregar_mascota, name='agregar_mascota'),
    path('lista/', views.lista_mascotas, name='lista_mascotas'),
]