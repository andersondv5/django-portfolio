from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import ContatoForm
from .forms import FormCadastro, FormLogin
from .models import Projeto

# view de projetos na tela de home, onde limita a exibição de projetos para no máximo de 3
def home(request):
    projetos_home = Projeto.objects.all()[:3]
    return render(request, 'home.html', {'projetos': projetos_home})


#view para formulário de contato que direciona para contato_sucesso.html
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

#view para sessão de projetos, mostram todos os projetos listados que foram adicionados no admin
def projetos_view(request):
    busca = request.GET.get('busca', '')
    ordenar_por = request.GET.get('ordenar_por', 'titulo')

    projetos = Projeto.objects.all()

    if busca:
        projetos = projetos.filter(titulo__icontains=busca)

    if ordenar_por in ['titulo']:
        projetos = projetos.order_by(ordenar_por)

    return render(request, 'projetos.html', {'projetos': projetos})

# view para sessão de cadastro
def cadastro_view(request):
    if request.method == 'POST':
        form = FormCadastro(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('home')
    else:
        form = FormCadastro()
    return render(request, 'cadastro.html', {'form': form})

# view para a tela de login
def login_view(request):
    if request.method == 'POST':
        form = FormLogin(data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect('home')
    else:
        form = FormLogin()
    return render(request, 'login.html', {'form': form})

# view para sessão de logout, quando o usuário clica em em "sair", é redirecionado para a tela de login novamente
def logout_view(request):
    logout(request)
    return redirect('login')
