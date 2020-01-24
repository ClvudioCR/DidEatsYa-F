from django.urls import path
from .views import *

app_name = 'tiendas'

urlpatterns = [
	path('',IndexView.as_view(), name='allstores'),
	path('<str:pk>/', DetailView.as_view(), name='details'),
	path('mantenedor/create/', TiendaCreate, name='crear'),
	path('mantenedor/buscar/', TiendaSearch, name='buscar'),
	path(r'mantenedor/editar/<pk>/', TiendaUpdate, name='editar'),
	path(r'mantenedor/Eliminar/<pk>/', TiendaDelete, name='eliminar'),
]