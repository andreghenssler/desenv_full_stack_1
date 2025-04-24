<<<<<<< HEAD
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("pesquisas/", include("pesquisas.urls")),
    path("admin/", admin.site.urls),
]
=======
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("pesquisas/", include("pesquisas.urls")),
    path("admin/", admin.site.urls),
]
>>>>>>> d4f1ef3 (Aula 16-04)
