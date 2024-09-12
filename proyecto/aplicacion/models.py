from django.db import models

class Espacio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    capacidad = models.IntegerField()
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    espacio = models.ForeignKey('Espacio', on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()

    def __str__(self):
        return f'{self.cliente} - {self.espacio} ({self.fecha_inicio} - {self.fecha_fin})'

class Pago(models.Model):
    reserva = models.ForeignKey('Reserva', on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateTimeField()

    def __str__(self):
        return f'Pago para {self.reserva} - Monto: {self.monto}'

class Factura(models.Model):
    reserva = models.ForeignKey('Reserva', on_delete=models.CASCADE)
    fecha_emision = models.DateTimeField()
    total_facturado = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=[('Pendiente', 'Pendiente'), ('Pagada', 'Pagada'), ('Cancelada', 'Cancelada')])

    def __str__(self):
        return f'Factura para {self.reserva} - Total: {self.total_facturado} - Estado: {self.estado}'