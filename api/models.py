from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete

# Create your models here.
class Receta(models.Model):
    nombre = models.CharField(max_length=150)
    ingredientes = models.TextField()
    preparacion = models.TextField()
    imagen = models.ImageField(upload_to='recetas', null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']


class Paso(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, related_name='pasos')
    numero = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='pasos', null=True, blank=True)

    def __str__(self):
        return self.descripcion


class RecetaFavorita(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    favoritos = models.IntegerField(default=0)


def update_favoritas(sender, instance, **kwargs):
    count = instance.receta.recetas_favorita_set.all().count()
    instance.receta.favoritos = count
    instance.receta.save()

post_save.connect(update_favoritas, sender=RecetaFavorita)
post_delete.connect(update_favoritas, sender=RecetaFavorita)