# Anexo: Prompts utilizados con el agente de IA

A continuación quedan registrados los prompts que redacté y le entregué al agente
de inteligencia artificial para la actividad de la clínica veterinaria
"Huellas Sanas". Los tres prompts corresponden a las tres tareas que pedía el
encargo.

---

## Prompt 1 — Formulario y tabla en HTML/CSS responsivo

```
Hola, estoy haciendo una actividad de la universidad. Es un sistema web para
una clínica veterinaria que se llama "Huellas Sanas", hecho en Django.

Necesito que me ayudes a generar el código HTML y CSS (responsivo) de dos
partes de la interfaz:

1) El formulario para ingresar nuevos pacientes. Tiene que tener estos campos:
   - Nombre de la mascota
   - Especie
   - Raza
   - Nombre del dueño
   Con sus etiquetas (label), espacios para mostrar errores de validación si
   el usuario se equivoca, y el token CSRF de Django porque el form es con
   method="post".

2) La tabla que muestra el listado diario de citas. Columnas:
   - Hora
   - Paciente
   - Especie / Raza
   - Dueño
   - Motivo de consulta
   - Estado (que se vea con colores: pendiente amarillo, atendida verde,
     cancelada rojo)
   - Acciones (botones para marcar una cita como atendida o cancelada)

Porfa entrégame los archivos: base.html, lista_citas.html, crear_mascota.html
y estilos.css.
```


## Prompt 2 — Script de datos ficticios (20 pacientes y citas)

```
Continuando con la actividad de "Huellas Sanas": ya tengo los modelos en
Django creados en la app "citas":

- Mascota(nombre, especie, raza, nombre_dueno)
- Cita(mascota que es una clave foránea a Mascota, fecha, hora,
  motivo_consulta y estado que puede ser pendiente, atendida o cancelada)

Necesito un script en Python que me cargue datos ficticios para poder probar
el sistema, porque sin datos no se puede validar nada.

Requisitos del script:
- Que cree exactamente 20 pacientes (mascotas) con nombres de perros/gatos y
  apellidos de dueños chilenos realistas. Ojo: SIN tildes ni la ñ, porque
  antes tuve un problema de encoding y me aparecían signos de pregunta en
  la base de datos.
- Que cree citas para esas mascotas:
  * Al menos 10 citas para el día de hoy, así pruebo el listado diario.
  * El resto en días pasados y futuros (más menos 2 semanas).
  * Estados variados: harto pendiente, algunas atendidas y canceladas.
  * Horarios de 9:00 a 17:00 en media horas.
  * Motivos variados: vacunación, control de peso, baños, etc.
- Que no duplique datos si ya existe información en la base (lo del profe:
  que se pueda volver a correr sin que se llene de repetidos).
- Que imprima al final cuántos pacientes y citas creó.

Lo ejecuto con: pipenv run python generar_datos_ficticios.py
```

---

## Prompt 3 — Administrar las citas con Django

```
Ya tengo los datos ficticios cargados en "Huellas Sanas". Ahora me piden
administrar las citas que se generaron, pero usando el framework Django
(o sea, a través del código, no tocando la base de datos a mano).

Puedes ayudarme a implementarlo por estas dos formas que vimos en clases:

A) Con vistas y rutas de Django (para el recepcionista):
   - Una vista que muestre el listado de citas del día. Que se pueda cambiar
     la fecha con ?fecha=AAAA-MM-DD y que por defecto muestre hoy.
   - Un formulario para registrar pacientes nuevos (con ModelForm).
   - Una vista que reciba un POST y cambie el estado de una cita (atender,
     cancelar o reabrir), y después haga redirect al listado de esa fecha,
     mostrando un mensaje de éxito con django.contrib.messages.
   - Las URLs con include() y nombres para usar {% url %} en las plantillas.
Entrégame los archivos forms.py, views.py, urls.py y las plantillas.

