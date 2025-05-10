from django.shortcuts import render
from .models import Vaga, Candidato
from .forms import VagaForm, CandidatoForm

def index(request):
    vagas = Vaga.objects.all()
    return render(request, 'empregos/index.html', {'vagas': vagas})

def lista_candidatos(request):
    candidatos = Candidato.objects.all()
    return render(request, 'empregos/lista_candidatos.html', {'candidatos': candidatos})

def detalhes_candidato(request, candidato_id):
    candidato = Candidato.objects.get(id=candidato_id)
    return render(request, 'empregos/detalhes_candidato.html', {'candidato': candidato})

def detalhes_vaga(request, vaga_id):
    vaga = Vaga.objects.get(id=vaga_id)
    return render(request, 'empregos/detalhes_vaga.html', {'vaga': vaga})

def formulario_candidato(request):
    form = CandidatoForm()
    return render(request, 'empregos/formulario_candidato.html', {'form': form})

def formulario_vaga(request):
    form = VagaForm()
    return render(request, 'empregos/formulario_vaga.html', {'form': form})