from django.urls import path
from .import views

app_name = 'confcurso'

urlpatterns = [
    path('', views.restricoes, name='restricoes'),
]