
from django.shortcuts import render

import math

def index(request):
    context = {
        'titulo' : 'Formulario'
        }
    return render(request,'encuesta/formulario.html',context)

def enviar(request):
    context = {
        'titulo' : "Respuesta",
        'nombre' : request.POST['nombre'],
        'clave' : request.POST['password'],
        'educacion' : request.POST['educacion'],
        'idiomas' : request.POST.getlist('idiomas'),
        'correo' : request.POST['email'],
        'website' : request.POST['sitioweb'],
    }

    return render(request, 'encuesta/respuesta.html',context)

def problema1(request):
    context = {'title' : 'Problema propuesto 1'}
    return render(request,'encuesta/problema_1.html',context)

# funciones para sumar, restar o multiplicar
def suma(request,numero1,numero2):
    return int(numero1) + int(numero2)
def resta(request,numero1,numero2):
    return int(numero1) - int(numero2)
def multiplicacion(request,numero1,numero2):
    return int(numero1) * int(numero2)


def respuesta1(request):
    ope = {
        'numero1' : request.POST['numero1'],
        'numero2' : request.POST['numero2'], 
    }

    context = {
        'title' : request.POST['operacion'],
        'numero1' : request.POST['numero1'],
        'numero2' : request.POST['numero2'],
        'operacion' : request.POST.getlist('operacion'),
        'suma' : suma(request,ope['numero1'],ope['numero2']),
        'resta' : resta(request,ope['numero1'],ope['numero2']),
        'multiplicacion' : multiplicacion(request,ope['numero1'],ope['numero2']),
    }
    return render(request,'encuesta/respuesta_1.html',context)

def volumen(request,diametro,altura):
    diametro = float(diametro)
    altura = float(altura)

    radio = diametro / 2
    area_base = math.pi * (radio * radio)
    v = round(area_base * altura, 11)
    return v
    

def problema2(request):
    context = {'title' : 'CALCULO DEL VOLUMEN DE UN CILINDO'}
    return render(request,'encuesta/calculo_cilindro.html',context)

def respuesta2(request):
    ope = {
        'diametro' : request.POST['diametro'],
        'altura' : request.POST['altura'],
    }

    context = {
        'volumen' : volumen(request,ope['diametro'],ope['altura'])
    }

    return render(request,'encuesta/respuesta_cilindro.html',context)