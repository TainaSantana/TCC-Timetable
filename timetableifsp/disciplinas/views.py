from django.shortcuts import render

def discList(request):
    return render(request, 'disciplinas/discilist.html', {})

