from django.urls import path

from . import views

urlpatterns = [
    path("", views.cliente_list, name="index"),
    path("clientes/", views.cliente_list, name="cliente_list"),
    path("clientes/<int:pk>/", views.cliente_detail, name="cliente_detail"),
]
