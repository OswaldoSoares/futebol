from django.shortcuts import render
from core import facade

def index_core(request):
    contexto = facade.create_contexto_lista(request)
    return render(request, 'core/index.html', contexto)
