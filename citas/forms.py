from django import forms
from .models import Mascota


class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ["nombre", "especie", "raza", "nombre_dueno"]
        widgets = {
            "nombre": forms.TextInput(attrs={"placeholder": "Ej: Max"}),
            "especie": forms.TextInput(attrs={"placeholder": "Ej: Perro / Gato"}),
            "raza": forms.TextInput(attrs={"placeholder": "Ej: Labrador"}),
            "nombre_dueno": forms.TextInput(attrs={"placeholder": "Ej: Ana Perez"}),
        }
        labels = {
            "nombre": "Nombre de la mascota",
            "especie": "Especie",
            "raza": "Raza",
            "nombre_dueno": "Nombre del dueño",
        }
