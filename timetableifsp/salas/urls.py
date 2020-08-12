from django.urls import path
from .import views

app_name = 'salas'

urlpatterns = [
    path('cadastro/', views.salaList, name='sala-list'),
    
]