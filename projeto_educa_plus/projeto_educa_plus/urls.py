from django.contrib import admin
from django.urls import path
from app_educa_plus import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("login/", views.login, name="login"),
    path('sair/', views.sair, name='sair'),
    path("registro/", views.registro, name="registro"),
    path("painel/", views.painel, name="painel"),
    path("editar/", views.editar, name="editar"),
    path("sobre/", views.sobre, name="sobre"),
    path("cursos/", views.cursos, name="cursos"),
    path("video/", views.video, name="video")
]
