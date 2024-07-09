
from django.db import models

# Create your models here.

class Categoria(models.Model):
    id_categoria = models.AutoField(db_column="id_categoria",primary_key=True)
    categoria = models.CharField(max_length=50,blank=False,null=False)


    def __str__(self):
        return str(self.categoria)

class Juego(models.Model):
    id = models.CharField(primary_key=True,max_length=10)
    nombre = models.CharField(max_length=50)
    precio = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=500)
    id_categoria = models.ForeignKey("Categoria",on_delete=models.CASCADE,db_column="id_categoria")
    stock = models.CharField(max_length=3)
    activo = models.IntegerField()

    def __str__(self):
        return str(self.id) +" "+ str(self.nombre) 