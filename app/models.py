from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    telefono = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.email} {self.telefono}"

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100, null=True)
    telefono = models.CharField(max_length=100, null=True)

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField(null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombre} {self.precio} {self.stock}"
    