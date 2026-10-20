import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "huellas_sanas.settings")
django.setup()

from citas.models import Mascota

correcciones = {
    1: ("Labrador", "Ana Perez"),
    2: ("Siames", "Carlos Gomez"),
    3: ("Pastor Aleman", "Maria Lopez"),
    4: ("Comun Europeo", "Juan Rodriguez"),
    5: ("Bulldog", "Laura Martinez"),
}

for id_mascota, (raza, dueno) in correcciones.items():
    Mascota.objects.filter(id=id_mascota).update(raza=raza, nombre_dueno=dueno)

print("Datos corregidos:")
for m in Mascota.objects.all():
    print(f"  {m.nombre} | {m.raza} | {m.nombre_dueno}")
