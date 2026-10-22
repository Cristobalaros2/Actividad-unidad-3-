from django.urls import path

from . import views

urlpatterns = [
    path("", views.landing, name="landing"),
    path("citas/", views.lista_citas, name="lista_citas"),
    path("citas/paciente/nuevo/", views.crear_mascota, name="crear_mascota"),
    path(
        "citas/cita/<int:cita_id>/estado/",
        views.actualizar_estado_cita,
        name="actualizar_estado_cita",
    ),
]
