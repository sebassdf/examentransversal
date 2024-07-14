from django.shortcuts import render,redirect

from .cart import Cart
from shop.models import Producto


# Create your views here.

def agregar_producto(request,producto_id):
    cart= Cart(request)
    producto= Producto.objects.get(id=producto_id)

    cart.agregar(producto=producto)
    
    return redirect("Shop")



def eliminar_producto(request,producto_id):
    cart= Cart(request)
    producto= Producto.objects.get(id=producto_id)

    cart.eliminar_carrito(producto=producto)
    
    return redirect("Shop")





def restar_producto(request,producto_id):
    cart= Cart(request)
    producto= Producto.objects.get(id=producto_id)

    cart.restar_producto(producto=producto)
    
    return redirect("Shop")


def limpiar_carroproducto(request):
    cart= Cart(request)
    cart.limpiar_carrito()
    
    return redirect("Shop")

