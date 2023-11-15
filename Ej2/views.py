from django.shortcuts import render
from .forms import FormularioNombreCont
from django.utils import timezone


# Create your views here.
def formulario(request):
    if request.method == 'GET':
        form = FormularioNombreCont(request.GET)
        if form.is_valid():
            fecha = form.cleaned_data['fecha_acceso']
            user = form.cleaned_data['username']
            password = form.cleaned_data['password']
            return render(request, 'respuestaForm2.html',
                          {'fecha_acceso': fecha, 'usuario': user, 'password': password})
    form = FormularioNombreCont()
    form.fecha_acceso = timezone.now
    return render(request, 'form.html', {'form': form})
