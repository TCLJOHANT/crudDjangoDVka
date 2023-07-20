from django.shortcuts import render
from django.shortcuts import redirect
from .models import Personaje
from .forms import PersonajeForm

# Create your views here.
def index (request):
    return render(request, 'index/index.html')
def nosotros (request):
    return render (request, 'index/nosotros.html')
def personaje (request):
    personajes = Personaje.objects.all()
    return render(request, 'personajeDBall/index.html',{'personajes':personajes}) #mandar variable vista
def crear (request):
    formulario = PersonajeForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('personaje')
    return render(request,'personajeDBall/crear.html',{'formulario':formulario})

def editar (request,id):
    personaje = Personaje.objects.get(id=id)
    formulario = PersonajeForm(request.POST or None, request.FILES or None, instance=personaje)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('personaje')
    return render(request, 'personajeDBall/editar.html',{'formulario':formulario})

def eliminar (request,id):
    personaje = Personaje.objects.get(id=id)
    personaje.delete()
    return redirect('personaje')

