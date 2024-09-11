from django.contrib import admin
from .models import espacio, cliente, reserva, pago, factura

admin.site.register(espacio)
admin.site.register(cliente)
admin.site.register(reserva)
admin.site.register(pago)
admin.site.register(factura)