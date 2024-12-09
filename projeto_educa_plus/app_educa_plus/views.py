from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from .models import Estudante

def home(request):
    return render(request, "usuarios/home.html")

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha') 

        user = User.objects.get(email=email)
        user = authenticate(request, username=user.username, password=senha)
            
        if user is not None:
            auth_login(request, user)
            return redirect('painel')
        else:
            messages.error(request, 'Erro. Verifique os dados inseridos!.')
    else: 
        return render(request, "usuarios/login.html")
    

def registro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha') 

        if nome and email and senha:

            novo_usuario = User.objects.create_user(username=nome, email=email, password=senha)
            novo_usuario.save()

            Estudante.objects.create(
                user=novo_usuario,
                nome=nome,
                data_nascimento=request.POST.get('data-nascimento'),
                conquistas = 0,  # Campo adicional do formulário
                tipo_plano='EDUCABASIC'  # Campo adicional do formulário
            )

            messages.success(request, 'Usuário cadastrado com sucesso!')
            return render(request, 'usuarios/registro.html')

        else:
            messages.error(request, 'Por favor, preencha todos os campos.')
    else: 
        return render(request, "usuarios/registro.html")


def painel(request):
    usuario = request.user
    estudante = Estudante.objects.filter(user=usuario).first()

    return render(request, 'usuarios/meu-painel.html', {'usuario': usuario, 'estudante': estudante})

def editar(request):
    estudante = get_object_or_404(Estudante, user=request.user)

    if request.method == 'POST':
        nome = request.POST.get('nome')
        data_nascimento=request.POST.get('data-nascimento')
        
        if nome:
            estudante.nome = nome
        if data_nascimento:
            estudante.data_nascimento = data_nascimento
        
        estudante.save()

        return redirect('painel')
    else: 
        return render(request, 'usuarios/editar.html')

def sobre(request):
    return render(request, "usuarios/sobre.html")

def cursos(request):
    return render(request, "usuarios/cursos.html")

def video(request):
    return render(request, "usuarios/video.html")

def sair(request):
    logout(request)
    return redirect('login')