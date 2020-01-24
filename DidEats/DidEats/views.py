from django.shortcuts import render
from django.views import generic

def inicio(request):
	return render(
		request,
		'inicio.html',
		context={}
	)
