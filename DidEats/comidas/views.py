from django.shortcuts import render
from .models import Comida
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib import messages
from .forms import ComidaCreateForm
# Create your views here.

class IndexView(generic.ListView):
    model = Comida
    template_name = 'comidas/comidas_lista.html'
    def get_queryset(self):
        return Comida.objects.all() 

class DetailView(generic.DetailView):
	model = Comida

def ComidaCreate(request):
	form = ComidaCreateForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit = True)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		'title' : "Crear",
		'form':form
	}
	return render(request, 'comidas/comida_crear.html',context)

def ComidaSearch(request, id=None):

	queryset = Comida.objects.all()
	query = request.GET.get("q")
	if query:
			queryset = queryset.filter(comida_id__icontains=query)
	context = {
		"object_list" : queryset,
		"title" : "Buscar"
	}
	return render(request, "comidas/comidas_buscar.html",context)

def ComidaUpdate(request, pk = None):
    instance = get_object_or_404(Comida, comida_id = pk)
    form = ComidaCreateForm(request.POST or None, request.FILES or None,instance=instance)
    if form.is_valid():
        instance = form.save(commit=True)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": "Editar",
        "instance":instance,
        "form" : form
    }
    return render(request, "comidas/comida_crear.html",context)


def ComidaDelete(request, pk= None):
    instance = get_object_or_404(Comida, comida_id = pk)
    instance.delete()
    return redirect("comidas:buscar")