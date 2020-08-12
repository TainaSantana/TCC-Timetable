from django.urls import path
from .import views

app_name = 'disciplinas'

urlpatterns = [
    path('cadastro/', views.discList, name='disc-list'),
]