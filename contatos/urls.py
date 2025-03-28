from django.urls import path
from .views import home, lista_contatos, detalhe_contato, add_contato

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('contatos/', lista_contatos, name='lista_contatos'),
    path('contatos/<int:id>/', detalhe_contato, name='detalhe_contato'),
    path('add_contato/', add_contato, name='add_contato')
]
