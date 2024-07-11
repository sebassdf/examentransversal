
from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),

    path('crud', views.crud, name='crud'),
    path('juegosAdd', views.juegosAdd, name='juegosAdd'),
    path('juegosDel/<str:pk>', views.juegosDel, name='juegosDel'),
    path('juegosEdit/<str:pk>', views.juegosEdit, name='juegosEdit'),
    path('juegosUpdate', views.juegosUpdate, name='juegosUpdate'),
    


]

