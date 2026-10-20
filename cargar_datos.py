import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "huellas_sanas.settings")
django.setup()

from datetime import date, time
from citas.models import Mascota, Cita

if not Mascota.objects.exists():
    mascotas = [
        Mascota(nombre="Max", especie="Perro", raza="Labrador", nombre_dueno="Ana Perez"),
        Mascota(nombre="Luna", especie="Gato", raza="Siames", nombre_dueno="Carlos Gomez"),
        Mascota(nombre="Rex", especie="Perro", raza="Pastor Aleman", nombre_dueno="Maria Lopez"),
        Mascota(nombre="Mimi", especie="Gato", raza="Comun Europeo", nombre_dueno="Juan Rodriguez"),
        Mascota(nombre="Rocky", especie="Perro", raza="Bulldog", nombre_dueno="Laura Martinez"),
    ]
    Mascota.objects.bulk_create(mascotas)
    print("Mascotas creadas:", Mascota.objects.count())
else:
    print("Mascotas ya existentes:", Mascota.objects.count())

if not Cita.objects.exists():
    citas = [
        Cita(mascota=Mascota.objects.get(nombre="Max"), fecha=date(2026, 10, 20), hora=time(9, 0), motivo_consulta="Vacunación anual", estado="atendida"),
        Cita(mascota=Mascota.objects.get(nombre="Luna"), fecha=date(2026, 10, 21), hora=time(10, 30), motivo_consulta="Revisión de rutina", estado="pendiente"),
        Cita(mascota=Mascota.objects.get(nombre="Rex"), fecha=date(2026, 10, 21), hora=time(12, 0), motivo_consulta="Cojera en pata trasera", estado="pendiente"),
        Cita(mascota=Mascota.objects.get(nombre="Mimi"), fecha=date(2026, 10, 22), hora=time(15, 0), motivo_consulta="Problemas digestivos", estado="cancelada"),
        Cita(mascota=Mascota.objects.get(nombre="Rocky"), fecha=date(2026, 10, 23), hora=time(11, 0), motivo_consulta="Limpieza dental", estado="pendiente"),
        Cita(mascota=Mascota.objects.get(nombre="Max"), fecha=date(2026, 10, 25), hora=time(9, 30), motivo_consulta="Control de peso", estado="pendiente"),
    ]
    Cita.objects.bulk_create(citas)
    print("Citas creadas:", Cita.objects.count())
else:
    print("Citas ya existentes:", Cita.objects.count())
