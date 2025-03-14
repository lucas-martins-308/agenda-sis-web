from django.shortcuts import render
from .models import Contato

def home(request):
    return render(request, 'contatos/home.html')

def lista_contatos(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos/lista_contatos.html', {'contatos': contatos})

def detalhe_contato(request, id):
    contato = Contato.objects.filter(id=id).first() 
    return render(request, 'contatos/detalhe_contato.html', {'contato': contato})
