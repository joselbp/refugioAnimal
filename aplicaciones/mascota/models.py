from django.db import models
from aplicaciones.adopcion.models import Adoptante
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_delete
class Tipo(models.Model):
    nombre=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('tipo-list')
class Mascota(models.Model):
    adoptante=models.ForeignKey(Adoptante,null=True,blank=True,on_delete=models.PROTECT)
    tipo=models.ForeignKey(Tipo,null=True,blank=True,on_delete=models.PROTECT)
    nombre=models.CharField(max_length=50)
    sexo=models.CharField(max_length=15)
    edad=models.IntegerField()
    raza=models.CharField(max_length=50)
    foto=models.ImageField(upload_to='fotos')
    adoptado=models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

@receiver(post_delete, sender=Mascota)
def tipo_delete(sender, instance, **kwargs):
   
    instance.foto.delete(False)