from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('espacios/nuevo/', views.crear_espacio, name='crear_espacio'),
    path('clientes/nuevo/', views.crear_cliente, name='crear_cliente'),
    path('reservas/nueva/', views.crear_reserva, name='crear_reserva'),
    path('pagos/nuevo/', views.registrar_pago, name='registrar_pago'),
    path('eventos/', views.resumen_eventos, name='resumen_eventos'),
    path('cliente/<int:cliente_id>/historial/', views.historial_pagos_facturacion, name='historial_pagos_facturacion'),
    path('historial-pagos/', views.historial_pagos, name='historial_pagos'),
    path('historial-facturacion/', views.historial_facturacion, name='historial_facturacion'),
    path('crear-factura/', views.crear_factura, name='crear_factura'),
    path('resumen_eventos/', views.resumen_eventos, name='resumen_eventos'),
]