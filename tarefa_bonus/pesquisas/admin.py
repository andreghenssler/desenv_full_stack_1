<<<<<<< HEAD
from django.contrib import admin

from .models import Categoria, Produto

admin.site.register(Categoria)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome")

admin.site.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome",
                  "preco",
                  "descricao",
                  "categoria")
    list_filter = ('categoria',)

=======
from django.contrib import admin

from .models import Categoria, Produto

admin.site.register(Categoria)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome")

admin.site.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome",
                  "preco",
                  "descricao",
                  "categoria")
    list_filter = ('categoria',)

>>>>>>> d4f1ef3 (Aula 16-04)
