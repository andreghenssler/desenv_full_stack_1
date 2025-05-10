from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('candidatos/', views.lista_candidatos, name='lista_candidatos'),
    path('candidatos/<int:candidato_id>/', views.detalhes_candidato, name='detalhes_candidato'),
    path('vagas/<int:vaga_id>/', views.detalhes_vaga, name='detalhes_vaga'),
    path('candidatos/formulario/', views.formulario_candidato, name='formulario_candidato'),
    path('vagas/formulario/', views.formulario_vaga, name='formulario_vaga'),
]