from django.db import models


class Mascota(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre de la mascota")
    especie = models.CharField(max_length=50, verbose_name="Especie")
    raza = models.CharField(max_length=100, verbose_name="Raza")
    nombre_dueno = models.CharField(max_length=150, verbose_name="Nombre del dueño")

    class Meta:
        verbose_name = "Mascota"
        verbose_name_plural = "Mascotas"

    def __str__(self):
        return f"{self.nombre} ({self.especie} - {self.raza}) - Dueño: {self.nombre_dueno}"


class Cita(models.Model):
    ESTADO_CITAS = [
        ("pendiente", "Pendiente"),
        ("atendida", "Atendida"),
        ("cancelada", "Cancelada"),
    ]

    mascota = models.ForeignKey(
        Mascota,
        on_delete=models.CASCADE,
        related_name="citas",
        verbose_name="Mascota",
    )
    fecha = models.DateField(verbose_name="Fecha")
    hora = models.TimeField(verbose_name="Hora")
    motivo_consulta = models.TextField(verbose_name="Motivo de consulta")
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CITAS,
        default="pendiente",
        verbose_name="Estado",
    )

    class Meta:
        verbose_name = "Cita"
        verbose_name_plural = "Citas"
        ordering = ["fecha", "hora"]

    def __str__(self):
        return f"{self.mascota.nombre} - {self.fecha} {self.hora} [{self.get_estado_display()}]"
