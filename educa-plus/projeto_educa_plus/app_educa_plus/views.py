from django.shortcuts import render

def login(request):
    return render(request, 'usuarios/login.html')

def registro(request):
    return render(request, 'usuarios/registro.html')