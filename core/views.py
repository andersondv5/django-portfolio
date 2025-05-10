from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from .forms import ContatoForm
from .models import Projeto

# view para interface de home
def home(request):
    projetos_home = Projeto.objects.all()[:3]
    return render(request, 'home.html', {'projetos': projetos_home})


#view para formulário contato que direciona para contato_sucesso.html
def contato_view(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contato_sucesso')
    else:
        form = ContatoForm()

    return render(request, 'contato.html', {'form': form})

def contato_sucesso(request):
    return render(request, 'contato_sucesso.html')

#view para sessão de projetos
def projetos_view(request):
    projetos = Projeto.objects.all()
    return render(request, 'projetos.html', {'projetos': projetos})

