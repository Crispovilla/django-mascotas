from django.urls import path
from . import views

urlpatterns = [
    path('bienvenida/', views.bienvenida, name='bienvenida'),
    path('mascotas/', views.mascotas, name='mascotas'),
    path('saludo/<str:nombre>/', views.saludo, name='saludo'),
]