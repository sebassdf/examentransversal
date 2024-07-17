
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CategoriaProd(models.Model):
    nombre= models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name= "categoriaprod"
        verbose_name_plural="categoriasprod"

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre= models.CharField(max_length=50) 
    #autor= models.ForeignKey(User, on_delete=models.CASCADE)
    categorias= models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="shop/", null= True, blank=True)
    precio= models.FloatField()
    cantidad= models.BooleanField()

    created = models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name= "Producto"
        verbose_name_plural="Productos"

    def __str__(self):
        return self.nombre 