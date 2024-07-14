from django.urls import path

from autenticacion.views import Vregistro, cerrar_sesion, logeo
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', Vregistro.as_view(), name="Autenticacion"),
    path('cerrar_sesion', cerrar_sesion, name="cerrar_sesion"),
    path('logeo', logeo, name="logeo"),
    
    

]

#as_view para que lo muestre como una vista