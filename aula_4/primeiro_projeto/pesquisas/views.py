from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Olá, Você está na index do app pesquisas.")

def somar(request):
    a = 5
    b = 10
    resultado = a + b
    return HttpResponse(f"A soma de {a} e {b} é {resultado}.")