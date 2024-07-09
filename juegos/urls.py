
from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),

    path('crud', views.crud, name='crud'),
    path('juegosAdd', views.juegosAdd, name='juegosAdd'),
    path('juegosDel', views.juegosDel, name='juegosDel'),
    path('juegosEdit', views.juegosEdit, name='juegosEdit'),
    


]

