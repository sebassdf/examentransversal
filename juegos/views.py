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

        objCategoria=Categoria.objects.get(id_categoria = categorias)
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
    


    
def juegosDel(request,pk):
    context={}
    try:
        juego=Juego.objects.get(id=pk)

        juego.delete()
        mensaje="Eliminado satisfactoriamente su producto"
        juegos = Juego.objects.all()
        context = {'juegos': juegos, 'mensaje': mensaje}
        return render(request,'juegos/juegos_list.html',context)
    except:
        mensaje = "Error al eliminar el producto"
        juegos = Juego.objects.all()
        context = {'juegos':juegos,'mensaje':mensaje}
        return render(request, 'juegos/juegos_list.html', context)




    
def juegosEdit(request,pk):
    if pk != "":
        juego=Juego.objects.get(id=pk)
        categorias=Categoria.objects.all()

        print(type(juego.id_categoria.categoria))

        context = {'juego':juego, 'categorias':categorias}

        if juego:
            return render(request,'juegos/juegos_edit.html',context)
        else:
            context={'mensaje':"Error, id no existe"}
            return render(request,'juegos/juegos_edit.html',context)




def juegosUpdate(request):
    
    if request.method == "POST":
        
        id=request.POST["id"]
        nombre=request.POST["nombre"]
        precio=request.POST["precio"]
        descripcion=request.POST["descripcion"]
        categoria=request.POST["categoria"]
        stock=request.POST["stock"]
        activo="1"

        objCategoria=Categoria.objects.get(id_categoria = categoria)

        juego = Juego()
        juego.id=id
        juego.nombre=nombre
        juego.precio=precio
        juego.descripcion=descripcion
        juego.id_categoria=objCategoria
        juego.stock=stock
        juego.activo=1
        juego.save()

        categorias=Categoria.objects.all()
        context={'mensaje':"Ok, datos actializados",'categorias':categorias,'juego':juego}
        return render(request, "juegos/juegos_edit.html", context)
    else:
        juegos = Juego.objects.all()
        context = {'juegos':juegos}
        return render(request,'juegos/juegos_list.html', context)