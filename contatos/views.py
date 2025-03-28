from django.shortcuts import render
from .models import Contato, Categoria
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'contatos/home.html')


@login_required(login_url='login')
def lista_contatos(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos/lista_contatos.html', {'contatos': contatos})

@login_required(login_url='login')
def detalhe_contato(request, id):
    contato = Contato.objects.filter(id=id).first() 
    return render(request, 'contatos/detalhe_contato.html', {'contato': contato})

@login_required(login_url='login')
def add_contato(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        endereco = request.POST.get('endereco')
        categoria = request.POST.get('categoria')

        categoria_id = Categoria.objects.get(id=categoria)
        Contato.objects.create(
            nome=nome,
            telefone=telefone,
            email=email,
            endereco=endereco,
            categoria_id=categoria
        )
    categorias = Categoria.objects.all() 
    return render(request, 'contatos/add_contato.html', {'categorias': categorias})