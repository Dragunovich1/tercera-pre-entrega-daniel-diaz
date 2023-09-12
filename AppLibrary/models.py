from django.db import models
from datetime import datetime

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50, null=True)
    dni = models.IntegerField()
    
    def __str__(self):
        return f"Nombre: {self.nombre}  - Apellido: {self.apellido} - DNI:  {self.dni}"

class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50, null=True)
    dni = models.IntegerField()
    legajo = models.IntegerField()
    fecha_ingreso = models.DateField(null=True)
    
    def __str__(self):
        return f"Fecha de ingreso: {self.fecha_ingreso} - Legajo: {self.legajo}  - Nombre:  {self.nombre} - Apellido: {self.apellido}"
    
class Libro(models.Model):
    autor = models.CharField(max_length=40)
    nombre_libro = models.CharField(max_length=40)
    
    def __str__(self):
        return f"Autor: {self.autor} - Libro: {self.nombre_libro}"

class Audiovisual(models.Model):
    autor = models.CharField(max_length=10)
    nombre_material = models.CharField(max_length=30)

    def __str__(self):
        return f"Autor: {self.autor} Material Audiovisual: {self.nombre_material}"

    
    







    

