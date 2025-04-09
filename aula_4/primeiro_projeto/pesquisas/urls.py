from django.urls import path

from . import views

urlpatterns = [
    path("pesquisas/", views.index, name="index"),
    path("soma/", views.somar, name="somar"),
    
]