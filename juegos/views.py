from django.shortcuts import render

from .models import Juego,Categoria

# Create your views here.

def index(request):
    juegos=Juego.objects.all()
    context={"juegos":juegos}
    return render(request, 'juegos/index.html', context)

def crud(request):
    juegos= Juego.objects.all()
    context={"juegos":juegos}
    return render (request, 'juegos/juegos_list.html', context)

def juegosAdd(request):
    if request.method is not "POST":
        categorias=Categoria.objects.all()
        context={'categorias':categorias}
        return render (request, 'juegos/juegos_add.html', context)
    else:
        id = request.POST ["id"]
        nombre = request.POST ["nombre"]
        precio = request.POST ["precio"]
        descripcion = request.POST ["descripcion"]
        id_categoria = request.POST ["id_categoria"]
        stock = request.POST ["stock"]
        activo = "1"

        objCategoria=Categoria.objects.get(id_categoria = categoria)
        obj=Juego.objects.create(id=id,
                                 nombre=nombre,
                                 precio=precio,
                                 descripcion=descripcion,
                                 id_categoria=objCategoria,
                                 stock=stock,
                                 activo=1)
        obj.save()
        context= {'mensaje' :"Datos guardados." }
        return render (request, 'juegos/juegos_add.html', context)
    


    
def juegosDel(request):
    if request.method is not "POST":
        categorias=Categoria.objects.all()
        context={'categorias':categorias}
        return render (request, 'juegos/juegos_list.html', context)
    
def juegosEdit(request):
    if request.method is not "POST":
        categorias=Categoria.objects.all()
        context={'categorias':categorias}
        return render (request, 'juegos/juegos_edit.html', context)