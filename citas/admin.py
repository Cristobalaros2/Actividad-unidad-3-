from django.contrib import admin
from .models import Mascota, Cita


@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "especie", "raza", "nombre_dueno")
    search_fields = ("nombre", "especie", "raza", "nombre_dueno")
    list_filter = ("especie", "raza")


@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ("id", "mascota", "fecha", "hora", "motivo_consulta", "estado")
    list_filter = ("estado", "fecha")
    search_fields = ("mascota__nombre", "mascota__nombre_dueno", "motivo_consulta")
    date_hierarchy = "fecha"
    list_editable = ("estado",)
    autocomplete_fields = ("mascota",)
