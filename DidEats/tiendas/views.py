from django.shortcuts import render
from .models import Tienda
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib import messages
from .forms import TiendaCreateForm
# Create your views here.

class IndexView(generic.ListView):
    model = Tienda
    template_name = 'tiendas/tiendas_lista.html'
    def get_queryset(self):
        return Tienda.objects.all() 

class DetailView(generic.DetailView):
	model = Tienda

def TiendaCreate(request):
	form = TiendaCreateForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit = True)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		'title' : "Crear",
		'form':form
	}
	return render(request, 'tiendas/tienda_crear.html',context)

def TiendaSearch(request, id=None):

	queryset = Tienda.objects.all()
	query = request.GET.get("q")
	if query:
			queryset = queryset.filter(tienda_id__icontains=query)
	context = {
		"object_list" : queryset,
		"title" : "Buscar"
	}
	return render(request, "tiendas/tiendas_buscar.html",context)

def TiendaUpdate(request, pk = None):
    instance = get_object_or_404(Tienda, tienda_id = pk)
    form = TiendaCreateForm(request.POST or None, request.FILES or None,instance=instance)
    if form.is_valid():
        instance = form.save(commit=True)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": "Editar",
        "instance":instance,
        "form" : form
    }
    return render(request, "tiendas/tienda_crear.html",context)


def TiendaDelete(request, pk= None):
    instance = get_object_or_404(Tienda, tienda_id = pk)
    instance.delete()
    return redirect("tiendas:buscar")