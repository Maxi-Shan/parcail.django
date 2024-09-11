from django import forms
from .models import espacio, cliente, reserva, pago, factura

class espacioForm(forms.ModelForm):
    class Meta:
        model = espacio
        fields = ['id', 'nombre', 'capacidad','tipo']

class clienteForm(forms.ModelForm):
    class Meta:
        model =  cliente
        fields = ['id', 'nombre' 'gmail', 'telefono']

class reservaForm(forms.ModelForm):
    class Meta:
        model = reserva
        fields = ['id','cliente','espacio','fecha_inicio','fecha_fin','total']

class pagoForm(forms.ModelForm):
    class Meta:
        model = pago
        fields = ['id','cliente','monto','fecha_pago']

class facturaForm(forms.ModelForm):
    class Meta:
        model = factura
        fields = ['id','reserva','fecha_emision','fecha_facturado','estado']