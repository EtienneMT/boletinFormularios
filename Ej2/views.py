from django.shortcuts import render
from .forms import FormularioNombreCont
from django.utils import timezone


# Create your views here.
def formulario(request):
    if request.method == 'GET':
        form = FormularioNombreCont(request.GET)
        if form.is_valid():
            form.fecha_acceso = timezone.now
            return render(request, 'respuestaForm2.html', {'form': form})
    form = FormularioNombreCont()
    form.fecha_acceso = timezone.now
    return render(request, 'form.html', {'form': form})
