from django.shortcuts import render
from .forms import FormularioFechaEmail


# Create your views here.
def welcome(request):
    return render(request, 'index.html', {})


def formulario(request):
    form = FormularioFechaEmail()
    if request.method == 'GET':
        form = FormularioFechaEmail(request.GET)
        if form.is_valid():
            return render(request, 'respuestaForm1.html', {'form': form})
    return render(request, 'form.html', {'form': form})
