from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<contato_id>', views.detalhes, name='detalhes'),
    path('busca/', views.busca, name='busca'),
]
