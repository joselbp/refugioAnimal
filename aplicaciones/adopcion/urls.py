from django.urls import path
from aplicaciones.adopcion.views import index_adopcion

urlpatterns = [
    path('index/', index_adopcion),
]