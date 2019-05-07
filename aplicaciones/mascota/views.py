from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Mascota, Tipo
from django.views.generic.edit import UpdateView, CreateView, DeleteView 
from django.urls import reverse_lazy
from rest_framework import viewsets
from .serializer import TipoSerializer, MascotaSerializer

# Create your views here.

def first_view(request):
    return render(request, 'base.html') 
def tipo(request):
    tipo_list = Tipo.objects.all()
    context = {'object_list': tipo_list}
    return render(request, 'mascota/tipo.html', context)

def tipo_detail(request, tipo_id):
    tipo = Tipo.objects.get(id=tipo_id)
    context = {'object': tipo}
    return render(request, 'mascota/tipo_detail.html', context)

def mascota_view(request):
    if request.method=='POST':
        form=MascotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('base:base')
    else:
        form=MascotaForm()
    
    return render(request,'mascota/mascota_form.html',{'form':form})
#Listar Mascotas
class MascotaListView(ListView):
    models=Mascota
    template='mascota/mascota_list.html'

#Detallar Mascota
class MascotaDetailView(DetailView):
    model = Mascota


#Actualizar Mascota
class MascotaUpdate(UpdateView):
	model = Mascota


#Crear Mascota
class MascotaCreate(CreateView):
	model = Mascota
	fields = '__all__'


#Eliminar Mascota
class MascotaDelete(DeleteView):
    model = Mascota
    success_url = reverse_lazy('mascota-list')
    
def base(request):
    return render(request, 'base/base.html')

class TipoList(viewsets.ModelViewSet):
	queryset=Tipo.objects.all()
	serializer_class=TipoSerializer

class MascotaList(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer