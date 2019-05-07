from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView
from .models import Adoptante
from django.views.generic.edit import UpdateView, CreateView, DeleteView 
from django.urls import reverse_lazy
# Create your views here.

def index_adopcion(request):
    return HttpResponse("Se supone aqui deberia estar la vista de los adoptantes")

#Listar adoptante
class AdoptanteList(ListView):
    models=Adoptante
    template='mascota/mascota_list.html'

#Detallar adoptante
class AdoptanteDetailView(DetailView):
    model = Adoptante

#Eliminar adoptante
class AdoptanteDelete(DeleteView):
    model = Adoptante
    success_url = reverse_lazy('adoptante-list')

#Actualizar adoptante
class AdoptanteUpdate(UpdateView):
	model = Adoptante

