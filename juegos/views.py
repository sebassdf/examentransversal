from django.shortcuts import render

from .models import Juego,Categoria

# Create your views here.

def index(request):
    juegos=Juego.objects.all()
    context={"juegos":juegos}
    return render(request, 'juegos/index.html', context)
