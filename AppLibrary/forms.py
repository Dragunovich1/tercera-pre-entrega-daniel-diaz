from django import forms


class ClienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=50, label="Nombre", widget=forms.TextInput(attrs={'class': 'alineacion-horizontal'}))
    apellido = forms.CharField(max_length=50 , label="Apellido", widget=forms.TextInput(attrs={'class': 'alineacion-horizontal'}))
    dni = forms.IntegerField(label="DNI", widget=forms.TextInput(attrs={'class': 'alineacion-horizontal'}))
    
class EmpleadoFormulario(forms.Form):
    nombre = forms.CharField(max_length=50, label="Nombre", widget=forms.TextInput(attrs={'class': 'alineacion-horizontal'}))
    apellido = forms.CharField(max_length=50 , label="Apellido", widget=forms.TextInput(attrs={'class': 'alineacion-horizontal'}))
    dni = forms.IntegerField(label="DNI", widget=forms.TextInput(attrs={'class': 'alineacion-horizontal'}))
    legajo = forms.IntegerField(label="Legajo", widget=forms.TextInput(attrs={'class': 'alineacion-horizontal'})) 
    fecha_ingreso = forms.DateField(label="Fecha de Ingreso", widget=forms.TextInput(attrs={'class': 'alineacion-horizontal'}))

class LibroFormulario(forms.Form):
    autor = forms.CharField(max_length=50, label="Autor", widget=forms.TextInput(attrs={'class': 'alineacion-horizontal'}))
    nombre_libro = forms.CharField(max_length=50 , label="Libro", widget=forms.TextInput(attrs={'class': 'alineacion-horizontal'}))

class AudiovisualFormulario(forms.Form):
    autor = forms.CharField(max_length=50, label="Autor", widget=forms.TextInput(attrs={'class': 'alineacion-horizontal'}))
    nombre_material = forms.CharField(max_length=50 , label="Material Audiovisual", widget=forms.TextInput(attrs={'class': 'alineacion-horizontal'}))
   

  