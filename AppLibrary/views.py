from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.http import HttpResponse,HttpRequest
from AppLibrary.models import Cliente,Empleado,Libro,Audiovisual
from django.db.models import Q
from .forms import ClienteFormulario, EmpleadoFormulario,LibroFormulario,AudiovisualFormulario


# Create your views here.
def inicio(request):
    return render(request, "inicio.html")


def listaClientes(request):
    listaClientes=Cliente.objects.all()
    return render(request, "listaClientes.html", {"listaClientes":listaClientes})

def listaEmpleados(request):
    listaEmpleados=Empleado.objects.all()
    return render(request, "listaEmpleados.html", {"listaEmpleados":listaEmpleados})

def listaLibros(request):
    listaLibros=Libro.objects.all()
    return render(request, "listaLibros.html", {"listaLibros":listaLibros})

def listaAudiovisuales(request):
    listaAudiovisuales=Audiovisual.objects.all()
    return render(request, "listaAudiovisuales.html", {"listaAudiovisuales":listaAudiovisuales})

def clientesFormulario(request):
    if request.method == "POST":
        cliFormulario = ClienteFormulario(request.POST)
        if cliFormulario.is_valid():
            data = cliFormulario.cleaned_data
            nuevo_cliente = Cliente(nombre=data["nombre"], apellido=data["apellido"], dni=data["dni"])
            nuevo_cliente.save()
            return render(request, "inicio.html")
    else:
        cliFormulario = ClienteFormulario()
        return render(request, "ClientesFormulario.html", {"cliFormulario": cliFormulario})

def empleadosFormulario(request):
    if request.method == "POST":
        empleadFormulario = EmpleadoFormulario(request.POST)
        if empleadFormulario.is_valid():
            data = empleadFormulario.cleaned_data
            nuevo_empleado = Empleado(nombre=data["nombre"], apellido=data["apellido"], dni=data["dni"], legajo=data["legajo"], fecha_ingreso=data["fecha_ingreso"])
            nuevo_empleado.save()

            # Agregar un mensaje de éxito
            messages.success(request, 'Empleado cargado exitosamente.')

            return redirect('inicio')  # Redirigir a la página de inicio u otra página que desees
    else:
        empleadFormulario = EmpleadoFormulario()
    return render(request, "empleadosFormulario.html", {"empleadFormulario": empleadFormulario})

    

def librosFormulario(request):
    if request.method == "POST":
        libFormulario = LibroFormulario(request.POST)
        if libFormulario.is_valid():
            data = libFormulario.cleaned_data
            nuevo_libro = Libro(autor=data["autor"], nombre_libro=data["nombre_libro"])  # Cambia el nombre de las claves para que coincidan con el formulario
            nuevo_libro.save()

            # Agregar un mensaje de éxito
            messages.success(request, 'Libro cargado exitosamente.')

            return redirect('inicio')  # Redirigir a la página de inicio u otra página que desees
    else:
        libFormulario = LibroFormulario()
    return render(request, "LibrosFormulario.html", {"libFormulario": libFormulario})

    
def audiovisualesFormulario(request):
    if request.method == "POST":
        audFormulario = AudiovisualFormulario(request.POST)
        if audFormulario.is_valid():
            data = audFormulario.cleaned_data
            nuevo_audiovisual = Audiovisual(autor=data["autor"], nombre_material=data["nombre_material"])
            nuevo_audiovisual.save()

            # Agregar un mensaje de éxito
            messages.success(request, 'Material audiovisual cargado exitosamente.')

            return redirect('inicio')  # Redirigir a la página de inicio u otra página que desees
    else:
        audFormulario = AudiovisualFormulario()
    return render(request, "audiovisualesFormulario.html", {"audFormulario": audFormulario})
    
    
def busquedaClientes(request):
    return render(request,"busquedaClientes.html")

def busquedaEmpleados(request):
    return render(request,"busquedaEmpleados.html")

def busquedaLibros(request):
    return render(request,"busquedaLibros.html")

def busquedaAudiovisuales(request):
    return render(request,"busquedaAudiovisuales.html")


from django.db.models import Q

def buscarCliente(request):
    try:
        query = request.GET.get("busca_nombre", "").strip()
        if query:
            clientes = Cliente.objects.filter(
                Q(nombre__icontains=query) |
                Q(apellido__icontains=query) |
                Q(dni__icontains=query)
            )
            if clientes.exists():
                return render(request, "resultadosBusquedaCliente.html", {"cliente": clientes})
            else:
                return HttpResponse("No se encontraron clientes con la búsqueda especificada")
        else:
            return HttpResponse("Ingrese un término válido para buscar clientes")
    except Exception as e:
        return HttpResponse(f"Error al buscar clientes: {str(e)}")

def buscar(request):
    try:
        query = request.GET.get("busca_nombre", "").strip()
        if query:
            empleados = Empleado.objects.filter(
                Q(nombre__icontains=query) |
                Q(apellido__icontains=query) |
                Q(dni__icontains=query) |
                Q(legajo__icontains=query)
            )
            if empleados.exists():
                return render(request, "resultadosBusqueda.html", {"empleado": empleados})
            else:
                return HttpResponse("No se encontraron empleados con la búsqueda especificada")
        else:
            return HttpResponse("Ingrese un término válido para buscar empleados")
    except Exception as e:
        return HttpResponse(f"Error al buscar empleados: {str(e)}")

def buscarLibro(request):
    try:
        query = request.GET.get("busca_titulo", "").strip()
        if query:
            libros = Libro.objects.filter(
                Q(autor__icontains=query) |
                Q(nombre_libro__icontains=query)
            )
            if libros.exists():
                return render(request, "resultadosBusquedaLibros.html", {"libro": libros})
            else:
                return HttpResponse("No se encontraron libros con la búsqueda especificada")
        else:
            return HttpResponse("Ingrese un título válido para buscar libros")
    except Exception as e:
        return HttpResponse(f"Error al buscar libros: {str(e)}")


def buscarAudiovisual(request):
    try:
        query = request.GET.get("busca_nombre", "").strip()
        if query:
            audiovisual = Audiovisual.objects.filter(
                Q(autor__icontains=query) |
                Q(nombre_material__icontains=query)
            )
            if audiovisual.exists():
                return render(request, "resultadosBusquedaAudiovisual.html", {"audiovisual": audiovisual})
            else:
                return HttpResponse("No se encontró material audiovisual con la búsqueda especificada")
        else:
            return HttpResponse("Ingrese un término válido para buscar material audiovisual")
    except Exception as e:
        return HttpResponse(f"Error al buscar material audiovisual: {str(e)}")

