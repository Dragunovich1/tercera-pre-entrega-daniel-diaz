from django.contrib import admin
from .models import Cliente,Empleado,Libro,Audiovisual
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Libro)
admin.site.register(Audiovisual)