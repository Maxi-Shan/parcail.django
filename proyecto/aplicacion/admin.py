from django.contrib import admin
from .models import Espacio, Cliente, Reserva, Pago, Factura

admin.site.register(Espacio)
admin.site.register(Cliente)
admin.site.register(Reserva)
admin.site.register(Pago)
admin.site.register(Factura)