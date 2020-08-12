from django.urls import path
from .import views

app_name = 'turmas'

urlpatterns = [
    path('cadastro/', views.turmaList, name='turma-list'),
    
]