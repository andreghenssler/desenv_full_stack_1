<<<<<<< HEAD
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Olá, Você está na index do app pesquisas.")

def somar(request):
    a = 5
    b = 10
    resultado = a + b
=======
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Olá, Você está na index do app pesquisas.")

def somar(request):
    a = 5
    b = 10
    resultado = a + b
>>>>>>> d4f1ef3 (Aula 16-04)
    return HttpResponse(f"A soma de {a} e {b} é {resultado}.")