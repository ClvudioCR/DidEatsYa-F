from django.urls import path
from .views import *

app_name='comidas'

urlpatterns = [
	path('',IndexView.as_view(), name='allfoods'),
	path('<str:pk>/', DetailView.as_view(), name='details'),
	path('mantenedor/create/', ComidaCreate, name='crear'),
	path('mantenedor/buscar/', ComidaSearch, name='buscar'),
	path(r'mantenedor/editar/<pk>/', ComidaUpdate, name='editar'),
	path(r'mantenedor/Eliminar/<pk>/', ComidaDelete, name='eliminar'),
]