from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import TurmaForm
from .models import Turma

def turmaList(request):
    turmas_list = Turma.objects.all()
    return render(request, 'turmas/turmalist.html', {'turmas_list': turmas_list})

def exibeTurma(request, id):
    turma = get_object_or_404(Turma, pk=id)
    return render(request, 'turmas/exibeturma.html', {'turma': turma})

def turmaCad(request):
   
    if request.method == 'POST':
        form = TurmaForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            status = form.cleaned_data['status']
            turma = form.save(commit=True)
            turma.save()
            return HttpResponseRedirect('/')
    else:
        form = TurmaForm
    return render(request, 'turmas/turmacadastro.html', {'form': form})

def deleteTurma(request, id):
    turma = get_object_or_404(Turma, pk=id)
    turma.delete()
    messages.info(request, 'Turma deletada com sucesso!')
    return redirect('turmas/turmalist.html')

def editaTurma(request, id):
    turma = get_object_or_404(Turma, pk=id)
    form = TurmaForm(instance=turma)

    if request.method == 'POST':
        form = TurmaForm(request.POST, instance=turma)

        if form.is_valid():
            turma.save()
            return redirect('/')
        else:
            return render(request, 'turmas/editaturma.html', {'form': form, 'turma': turma})
        
    else:
        return render(request, 'turmas/editaturma.html', {'form': form, 'turma': turma})



