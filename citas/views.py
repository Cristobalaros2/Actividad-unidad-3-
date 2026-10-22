from datetime import datetime, timedelta

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone

from .forms import MascotaForm
from .models import Cita, Mascota


def landing(request):
    """Página principal (landing) de la clínica Huellas Sanas."""
    return render(request, "citas/landing.html")


def lista_citas(request):
    """Listado diario de citas. Por defecto muestra las citas de hoy."""
    hoy = timezone.localdate()
    fecha_param = request.GET.get("fecha", "")

    if fecha_param:
        try:
            fecha = datetime.strptime(fecha_param, "%Y-%m-%d").date()
        except ValueError:
            fecha = hoy
    else:
        fecha = hoy

    citas = (
        Cita.objects.select_related("mascota")
        .filter(fecha=fecha)
        .order_by("hora")
    )

    context = {
        "citas": citas,
        "fecha": fecha,
        "hoy": hoy,
        "total": citas.count(),
        "dia_anterior": fecha - timedelta(days=1),
        "dia_siguiente": fecha + timedelta(days=1),
    }
    return render(request, "citas/lista_citas.html", context)


def crear_mascota(request):
    """Formulario para ingresar un nuevo paciente a la base de datos."""
    if request.method == "POST":
        form = MascotaForm(request.POST)
        if form.is_valid():
            mascota = form.save()
            messages.success(
                request,
                f"Paciente '{mascota.nombre}' registrado correctamente.",
            )
            return redirect("lista_citas")
    else:
        form = MascotaForm()

    return render(request, "citas/crear_mascota.html", {"form": form})


def actualizar_estado_cita(request, cita_id):
    """Administra el estado de una cita (atender / cancelar / reabrir)."""
    if request.method != "POST":
        return redirect("lista_citas")

    cita = get_object_or_404(Cita, id=cita_id)
    nuevo_estado = request.POST.get("estado")
    estados_validos = dict(Cita.ESTADO_CITAS)

    if nuevo_estado in estados_validos:
        cita.estado = nuevo_estado
        cita.save(update_fields=["estado"])
        messages.success(
            request,
            f"Cita de {cita.mascota.nombre} ({cita.hora.strftime('%H:%M')}) "
            f"marcada como {estados_validos[nuevo_estado].lower()}.",
        )

    fecha = request.POST.get("fecha") or cita.fecha.isoformat()
    return redirect(f"{reverse('lista_citas')}?fecha={fecha}")
