from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .forms import EspacioForm, ClienteForm, ReservaForm, PagoForm, FacturaForm
from .models import Reserva, Cliente, Pago, Factura, Espacio

def inicio(request):
    return render(request, 'inicio.html')

def crear_espacio(request):
    if request.method == 'POST':
        form = EspacioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resumen_eventos') 
    else:
        form = EspacioForm()

    return render(request, 'crear_espacio.html', {'form': form})

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resumen_eventos')  
    else:
        form = ClienteForm()

    return render(request, 'crear_cliente.html', {'form': form})


def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resumen_eventos')  
    else:
        form = ReservaForm()

    return render(request, 'crear_reserva.html', {'form': form})


def registrar_pago(request):
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resumen_eventos') 
    else:
        form = PagoForm()

    return render(request, 'registrar_pago.html', {'form': form})

def crear_factura(request):
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('historial_facturacion')  
    else:
        form = FacturaForm()

    context = {
        'form': form
    }
    return render(request, 'crear_factura.html', context)

def resumen_eventos(request):
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')
    espacio_id = request.GET.get('espacio')

    reservas = Reserva.objects.all()

    if fecha_inicio and fecha_fin:
        reservas = reservas.filter(
            Q(fecha_inicio__gte=fecha_inicio) & Q(fecha_fin__lte=fecha_fin)
        )
    
    if espacio_id:
        reservas = reservas.filter(espacio_id=espacio_id)

    espacios = Espacio.objects.all()

    for reserva in reservas:
        factura = reserva.factura_set.last()  # 
        if factura:
            reserva.estado_factura = factura.estado  
        else:
            reserva.estado_factura = 'Pendiente'

    return render(request, 'resumen_eventos.html', {
        'reservas': reservas,
        'espacios': espacios
    })

def historial_pagos_facturacion(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    pagos = Pago.objects.filter(reserva__cliente=cliente)
    facturas = Factura.objects.filter(reserva__cliente=cliente)

    contexto = {
        'cliente': cliente,
        'pagos': pagos,
        'facturas': facturas
    }
    
    return render(request, 'historial_pagos_facturacion.html', contexto)

def historial_pagos(request):
    pagos = Pago.objects.select_related('reserva').all()
    context = {
        'pagos': pagos,
    }
    return render(request, 'historial_pagos.html', context)

def historial_facturacion(request):
    facturas = Factura.objects.select_related('reserva').all()
    context = {
        'facturas': facturas,
    }
    return render(request, 'historial_facturacion.html', context)