from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

def login(request):
    if request.method == "POST":
        usuario = request.POST['usuario']    
        senha = request.POST['senha']    
        
        verificar_usuario = auth.authenticate(
            username=usuario,
            password=senha
        ) 
        
        if(verificar_usuario != None):
            auth.login(request, verificar_usuario)
            return redirect('home')
        else:
            print('Usuario ou senha incorreto')
            return render(request, 'pages/login.html')
        
    else:
        return render(request,'pages/login.html')

def register(request):
    
    if request.method == 'POST':
         usuario = request.POST['usuario']    
         email = request.POST['email']    
         senha = request.POST['senha']    
         confirmar_senha = request.POST['confirmar_senha']    
        
         User.objects.create_user(
            username=usuario,
            email=email,
            password=senha
        
        )
         return redirect('login')
    else:
        return render(request, 'pages/register.html')