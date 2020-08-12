from django.shortcuts import render

def profList(request):
    return render(request, 'professores/proflist.html', {})
