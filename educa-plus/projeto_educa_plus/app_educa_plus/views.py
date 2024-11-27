from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.decorators.http import require_POST

def login(request):
    return render(request, 'usuarios/login.html')

def registro(request):
    return render(request, 'usuarios/registro.html')

@require_POST
def login_usuario(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        
        user = User.objects.get(email=email)
        user = authenticate(request, username=user.username, password=senha)
        if user is not None:
            login(request, user)
            return redirect('painel')
        else:  
            return render(request, 'usuarios/login.gtml')
    
    

@require_POST
def cadastrar_usuario(request):
    try:
        usuario_aux = User.objects.get(email=request.POST['campo-email'])

        if usuario_aux:
            return render(request, 'usuarios/registro.html', {'msg': 'Erro! Já existe um usuário com o mesmo e-mail'})

    except User.DoesNotExist:
        nome_usuario = request.POST['nome-usuario']
        email = request.POST['email']
        senha = request.POST['senha']

        novoUsuario = User.objects.create_user(username=nome_usuario, email=email, password=senha)
        novoUsuario.save()
        
        return render(request, 'usuarios/login.html')
        
def painel(request):
    return render(request, 'usuarios/meu-painel.html')