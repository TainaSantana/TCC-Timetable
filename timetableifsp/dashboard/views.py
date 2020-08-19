from django.shortcuts import render
from django.http import HttpResponse
from professores.models import Professor
from disciplinas.models import Disciplina
from salas.models import Sala
import datetime

def index(request):

    prof = Professor.objects.all().count()
    disc = Disciplina.objects.all().count()
    salas = Sala.objects.all().count()
    return render(request, 'dashboard/index.html', {'prof': prof, 'disc': disc, 'salas': salas})
    
