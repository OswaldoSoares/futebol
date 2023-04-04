from django.shortcuts import render

def index_core(request):
    contexto = facade.create_contexto_inicial(request)
    return render(request, 'core/index.html', contexto)
