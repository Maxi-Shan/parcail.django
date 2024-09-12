from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Espacio, Cliente, Reserva, Pago, Factura

class EspacioForm(forms.ModelForm):
    class Meta:
        model = Espacio
        fields = ['nombre', 'capacidad', 'tipo']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono']

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['cliente', 'espacio', 'fecha_inicio', 'fecha_fin']
    
    fecha_inicio = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        label='Fecha y Hora de Inicio'
    )
    fecha_fin = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        label='Fecha y Hora de Fin'
    )

    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get("fecha_inicio")
        fecha_fin = cleaned_data.get("fecha_fin")

        if fecha_inicio and fecha_fin and fecha_inicio >= fecha_fin:
            raise ValidationError("La fecha y hora de fin deben ser posteriores a la fecha y hora de inicio.")

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['reserva', 'monto', 'fecha_pago']
    
    fecha_pago = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        label='Fecha y Hora del Pago'
    )

    def clean_fecha_pago(self):
        fecha_pago = self.cleaned_data.get('fecha_pago')
        if fecha_pago and fecha_pago > timezone.now():
            raise ValidationError("La fecha y hora del pago no pueden estar en el futuro.")
        return fecha_pago
    
class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['reserva', 'fecha_emision', 'total_facturado', 'estado']
    
    fecha_emision = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        label='Fecha y Hora de Emisión'
    )
