from django.urls import path
from . import views

urlpatterns=[
    path('listar/', views.listar_livros, name='listar_livros')
]