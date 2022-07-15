from mailbox import NoSuchMailboxError
from django.db import models
from django.forms import ModelChoiceField

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    precio = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="productos",null=True)

    def __str__(self):
        return self.nombre

opciones_consultas = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencias"],
    [3, "felicitaciones"],

]


class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre