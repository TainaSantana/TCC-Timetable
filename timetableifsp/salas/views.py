from django.shortcuts import render

def salaList(request):
    return render(request, 'salas/salalist.html', {})

