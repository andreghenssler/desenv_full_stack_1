<<<<<<< HEAD
from django.urls import path

from . import views

urlpatterns = [
    path("pesquisas/", views.index, name="index"),
    path("soma/", views.somar, name="somar"),
    
=======
from django.urls import path

from . import views

urlpatterns = [
    path("pesquisas/", views.index, name="index"),
    path("soma/", views.somar, name="somar"),
    
>>>>>>> d4f1ef3 (Aula 16-04)
]