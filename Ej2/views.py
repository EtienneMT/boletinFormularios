from django.shortcuts import render
from .forms import FormularioNombreCont


# Create your views here.
def formulario(request):
    form = FormularioNombreCont()
    if request.method == 'GET':
        form = FormularioNombreCont(request.GET)
        if form.is_valid():
            return render(request, 'respuestaForm1.html', {'form': form})
    return render(request, 'form.html', {'form': form})
