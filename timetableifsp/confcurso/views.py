from django.shortcuts import render

def restricoes(request):
    return render(request, 'confcurso/restricoes.html', {})
