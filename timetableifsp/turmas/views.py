from django.shortcuts import render

def turmaList(request):
    return render(request, 'turmas/turmalist.html', {})
