from django.shortcuts import render, redirect, get_object_or_404

from .models import reserva
from .forms import reservaForm

def pagina_principal(request):
    reservas = reserva.objects.all()
    return render(request, 'pagina_principal.html', {'reservas': reservas})

def gestion_reserva(request):
    reservas = reserva.objects.all()
    return render(request, 'gestion_reserva.html', {'reservas': reservas})

def crear_reserva(request):
    if request.method == 'POST':
        form = reservaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gestion_reserva')
    else:
        form = reservaForm()
    return render(request, 'formulario_reserva.html', {'form': form})

def modificar_reserva(request, id):
    reserva = get_object_or_404(reserva, id=id)
    if request.method == 'POST':
        form = reservaForm(request.POST, request.FILES, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('gestion_reserva')
    else:
        form = reservaForm(instance=reserva)
    return render(request, 'formulario_reserva.html', {'form': form})
