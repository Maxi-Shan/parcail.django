from django.db import models

class espacio(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    capacidad =models.IntegerField(max_length=5)
    tipo = models.CharField(max_length=255)

class cliente(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    gmail = models.EmailField(max_length=255)
    telefono = models.CharField(max_length=255)

class reserva(models.Model):
    id = models.IntegerField(primary_key=True)
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    espacio = models.ForeignKey(espacio, on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField(null=True, blank=True)
    fecha_fin = models.DateTimeField(null=True, blank=True)
    Total = models.DecimalField(max_digits=10, decimal_places=2)

class pago(models.Model):
    id = models.IntegerField(primary_key=True)
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateTimeField(null=True, blank=True)

class factura(models.Model):
    id = models.IntegerField(primary_key=True)
    reserva = models.ForeignKey(reserva, on_delete=models.CASCADE)
    fecha_emision = models.DateTimeField(null=True, blank=True)
    fecha_facturado = models.DateTimeField(null=True, blank=True)
    estado = models.CharField(max_length=255)