from django.contrib import admin
from .models import Contato, Categoria

admin.site.register(Categoria)

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'email', 'endereco')
    search_fields = ('nome', 'email', 'telefone')
    list_filter = ('nome',)
    
