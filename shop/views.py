
from django.shortcuts import render
from .models import Producto
from . import views
# Create your views here.


def shop(request):

    productos= Producto.objects.all()

    return render(request,"shop/shop.html", {"productos":productos})
