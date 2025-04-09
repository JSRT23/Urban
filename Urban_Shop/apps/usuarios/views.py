from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.hashers import check_password
from .models import Usuario

# Create your views here.
 

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            usuario = Usuario.objects.get(username=username)
        except Usuario.DoesNotExist:
            return render(request, 'login.html', {'message': 'Usuario no existe'})

        # Verificar contraseña usando la utilidad de Django
        if (password == usuario.password):
             # Manejo manual de sesión
            return redirect('index')
        else:
            return render(request, 'login.html', {'message': 'Contraseña incorrecta'})

    return render(request, 'login.html')
    
def registro_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        nombre = request.POST["name"]
        apellido = request.POST["apellido"]
        password = request.POST["password"]
        email = request.POST["gmail"]
        Usuario.objects.create(username=username, nombre=nombre, apellido=apellido, password=password, email=email)
        return HttpResponseRedirect(reverse("login"))
    else:
        return render(request, "registro.html")    
    
