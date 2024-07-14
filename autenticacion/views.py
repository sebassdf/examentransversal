from django.shortcuts import render, redirect
from django.views.generic import View

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate

from django.contrib import messages
# Create your views here.

class Vregistro(View):

    def get(self, request):
        form= UserCreationForm()
        return render(request,"autenticacion/autenticacion.html", {"form": form})
        

    def post(self, request):
        form= UserCreationForm(request.POST)
        if form.is_valid():
            usuario=  form.save()

            login(request,usuario)
        
            return redirect("Home")
        else:
            for msg in form.error_messages: #recorrer los posibles errores del form
                messages.error(request, form.error_messages[msg]) #mostrar errores del form, pasando el array

            return redirect("Home")
        

def cerrar_sesion(request):
    logout(request)
    return redirect("Home")

def logeo(request):
    if request.method=="POST":

        form =AuthenticationForm(request, data= request.POST)
        if form.is_valid():
            nombre_usuario= form.cleaned_data.get("username")
            contra_usuario= form.cleaned_data.get("password")
            usuario= authenticate(username=nombre_usuario, password=contra_usuario)
            if usuario is not None:
                login(request, usuario)
                return redirect("Home")
            else:
                messages.error(request, "Usuario no válido")
        
        else:
            messages.error(request, "Información Incorrecta")

    form =AuthenticationForm()
    return render(request,"login/login.html", {"form": form})  
