from django.urls import path
from .views import home, page, delete_cadastro, update
from .views import cadastro
from .views import listar

urlpatterns = [
    path('', home),
    path('page/', page),
    path('cadastro/', cadastro),
    path('lista/', listar),
    path('delete/<int:id>/', delete_cadastro, name='delete'),
    path('update/<int:id>/', update, name='update')
]
