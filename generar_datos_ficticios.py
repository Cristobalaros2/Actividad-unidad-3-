"""Genera datos ficticios para validar el sistema: 20 pacientes y sus citas.

Uso:
    pipenv run python generar_datos_ficticios.py
"""

import os
import random
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "huellas_sanas.settings")
django.setup()

from datetime import time, timedelta

from django.utils import timezone

from citas.models import Mascota, Cita

random.seed(42)

TOTAL_PACIENTES = 20

pacientes = [
    ("Toby", "Perro", "Beagle", "Camila Rojas"),
    ("Nala", "Gato", "Persa", "Diego Fernandez"),
    ("Simba", "Gato", "Bengali", "Valentina Soto"),
    ("Coco", "Loro", "Amazonico", "Rodrigo Munoz"),
    ("Lola", "Perro", "Poodle", "Fernanda Castro"),
    ("Tiger", "Gato", "Comun Europeo", "Nicolas Herrera"),
    ("Bella", "Perro", "Golden Retriever", "Antonia Vargas"),
    ("Michi", "Gato", "Siames", "Matias Silva"),
    ("Rocco", "Perro", "Husky", "Paula Contreras"),
    ("Kira", "Conejo", "Enano", "Jorge Alonso"),
    ("Bruno", "Perro", "Chihuahua", "Camila Fuentes"),
    ("Luna", "Gato", "Maine Coon", "Sebastian Reyes"),
    ("Teo", "Perro", "Mestizo", "Daniela Pino"),
    ("Nube", "Gato", "Sphynx", "Francisco Vega"),
    ("Maya", "Perro", "Border Collie", "Carla Munoz"),
    ("Pelusa", "Conejo", "Angora", "Andres Salinas"),
    ("Kaia", "Perro", "Pastor Aleman", "Josefina Braun"),
    ("Milo", "Gato", "Comun Europeo", "Pablo Sandoval"),
    ("Duna", "Perro", "Galgo", "Constanza Rojas"),
    ("Zoe", "Gato", "Ragdoll", "Felipe Araya"),
]

motivos = [
    "Vacunacion anual",
    "Control de peso",
    "Revision de rutina",
    "Baño y corte de uñas",
    "Desparasitacion",
    "Problemas digestivos",
    "Limpieza dental",
    "Vacunacion antirrabica",
    "Alergia en piel",
    "Cojera en pata delantera",
    "Control post operatorio",
    "Consulta general",
]

estados = ["pendiente", "pendiente", "pendiente", "atendida", "cancelada"]

hoy = timezone.localdate()

faltantes = TOTAL_PACIENTES - Mascota.objects.count()
if faltantes > 0:
    creadas = Mascota.objects.bulk_create(
        Mascota(nombre=n, especie=e, raza=r, nombre_dueno=d)
        for n, e, r, d in pacientes[:faltantes]
    )
    print(f"Pacientes nuevos creados: {len(creadas)}")
else:
    print("La base ya tiene 20 o más pacientes. No se agregan más.")

horas = [
    time(9, 0), time(9, 30), time(10, 0), time(10, 30),
    time(11, 0), time(11, 30), time(12, 0), time(12, 30),
    time(14, 0), time(14, 30), time(15, 0), time(15, 30),
    time(16, 0), time(16, 30), time(17, 0),
]

citas_hoy = Cita.objects.filter(fecha=hoy).count()
objetivo_hoy = 10

if citas_hoy >= objetivo_hoy:
    print(f"Citas de hoy ({hoy}): {citas_hoy}. No se agregan más para hoy.")
else:
    disponibles = list(
        Mascota.objects.exclude(citas__fecha=hoy).order_by("id")
        [: objetivo_hoy - citas_hoy]
    )
    horas_libres = [h for h in horas if not Cita.objects.filter(fecha=hoy, hora=h).exists()]
    nuevas_hoy = [
        Cita(
            mascota=mascota,
            fecha=hoy,
            hora=horas_libres[i],
            motivo_consulta=random.choice(motivos),
            estado="pendiente",
        )
        for i, mascota in enumerate(disponibles)
        if i < len(horas_libres)
    ]
    Cita.objects.bulk_create(nuevas_hoy)
    print(f"Citas de hoy agregadas: {len(nuevas_hoy)} (total hoy: {Cita.objects.filter(fecha=hoy).count()})")

if Cita.objects.count() < 30:
    mascotas = list(Mascota.objects.order_by("id"))
    extras = []
    for mascota in mascotas:
        existentes = Cita.objects.filter(mascota=mascota).count()
        for _ in range(max(0, random.randint(1, 2) - existentes)):
            dias = random.randint(-14, 14)
            if dias == 0:
                dias = 7
            extras.append(
                Cita(
                    mascota=mascota,
                    fecha=hoy + timedelta(days=dias),
                    hora=random.choice(horas),
                    motivo_consulta=random.choice(motivos),
                    estado=random.choice(estados),
                )
            )
    Cita.objects.bulk_create(extras)
    print(f"Citas históricas/futuras agregadas: {len(extras)}")

print(f"Totales -> Pacientes: {Mascota.objects.count()} | Citas: {Cita.objects.count()}")
