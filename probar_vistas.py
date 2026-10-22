import os
import django
import sys

sys.stdout.reconfigure(encoding="utf-8")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "huellas_sanas.settings")
django.setup()

from django.test import Client
from django.utils import timezone
from citas.models import Mascota, Cita

c = Client()

r = c.get("/")
print("GET / ->", r.status_code, r.headers.get("Location"))

r = c.get("/citas/")
print("GET /citas/ ->", r.status_code, "| tabla:", b"<table" in r.content, "| etiquetas estado:", r.content.count(b"etiqueta etiqueta-"))

r = c.get("/citas/paciente/nuevo/")
print("GET /citas/paciente/nuevo/ ->", r.status_code, "| form:", b"csrfmiddlewaretoken" in r.content)

antes = Mascota.objects.count()
r = c.post("/citas/paciente/nuevo/", {"nombre": "Prueba", "especie": "Perro", "raza": "Mestizo", "nombre_dueno": "Tester Uno"})
despues = Mascota.objects.count()
print("POST crear paciente ->", r.status_code, "| redirect:", r.headers.get("Location"), "| creada:", despues - antes == 1)
Mascota.objects.filter(nombre="Prueba").delete()

cita = Cita.objects.filter(fecha=timezone.localdate(), estado="pendiente").first()
r = c.post(f"/citas/cita/{cita.id}/estado/", {"estado": "atendida", "fecha": str(cita.fecha)})
cita.refresh_from_db()
print("POST atender cita ->", r.status_code, "| nuevo estado:", cita.estado)
cita.estado = "pendiente"
cita.save()

r = c.get("/citas/", {"fecha": "2026-10-21"})
print("GET /citas/?fecha=2026-10-21 ->", r.status_code)

r = c.get("/citas/paciente/nuevo/")
print("Plantilla formulario usa CSS:", b"estilos.css" in r.content)
