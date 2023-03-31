from django.urls import path

from . import views

app_name = 'encuesta'

urlpatterns = [
    path('',views.index,name='index'),
    path('enviar/',views.enviar,name='enviar'),
    # problema 1
    path('problema1/',views.problema1,name='problema1'),
    path('respuesta1/',views.respuesta1,name='respuesta1'),
    # problema 2
    path('problema2/',views.problema2,name='problema2'),
    path('respuesta2/',views.respuesta2,name='respuesta2'),
]