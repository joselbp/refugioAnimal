from django.db import models

# Create your models here.
class Adoptante(models.Model):
    nombre=models.CharField(max_length=50)
    edad=models.IntegerField()
    cel=models.CharField(max_length=15)
    email=models.EmailField()
    direccion=models.TextField()

    def __unicode__(self):
        return self.nombre