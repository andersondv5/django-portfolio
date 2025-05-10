from django.contrib import admin
from .models import Contato, Projeto

admin.site.register(Projeto)

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'mensagem', 'criado_em')
    search_fields = ('nome', 'email')