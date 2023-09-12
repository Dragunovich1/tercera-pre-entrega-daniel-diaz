
from django.urls import path
from AppLibrary.views import inicio,listaClientes,listaEmpleados,listaLibros,listaAudiovisuales,clientesFormulario,empleadosFormulario,librosFormulario,audiovisualesFormulario,busquedaEmpleados,busquedaClientes,busquedaLibros,busquedaAudiovisuales,buscar,buscarCliente,buscarLibro,buscarAudiovisual


urlpatterns = [
    path('', inicio, name="inicio"),
    path('listaClientes/',listaClientes, name="Clientes"),
    path('listaEmpleados/',listaEmpleados, name="Empleados"),
    path('listaLibros/',listaLibros, name="Libros"),
    path('listaAudiovisuales/',listaAudiovisuales, name="Audiovisuales"),
    path('clientesFormularios/',clientesFormulario, name="clientesFormularios"),
    path('empleadosFormularios/',empleadosFormulario, name="empleadosFormularios"),
    path('librosFormularios/',librosFormulario, name="librosFormularios"),
    path('audiovisualesFormularios/',audiovisualesFormulario, name="audiovisualesFormularios"),
    path('busquedaEmpleados/',busquedaEmpleados, name="BusquedaEmpleados"),
    path('busquedaClientes/',busquedaClientes, name="BusquedaClientes"),
    path('busquedaLibros/',busquedaLibros, name="BusquedaLibros"),
    path('busquedaAudiovisuales/',busquedaAudiovisuales, name="BusquedaAudiovisuales"),
    path('buscarCliente/',buscarCliente, name="BuscarCliente"),
    path('buscar/',buscar, name="Buscar"),
    path('buscarLibro/',buscarLibro, name="BuscarLibro"),
    path('buscarAudiovisual/',buscarAudiovisual, name="BuscarAudiovisual"),
]
