# from django.shortcuts import render
from django.shortcuts import render
from django.utils import timezone
from .models import Cliente

def index(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/cliente_list.html',{'clientes': clientes})

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/cliente_list.html', {'clientes': clientes})

def cliente_detail(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    return render(request, 'clientes/cliente_detail.html', {'cliente': cliente})
