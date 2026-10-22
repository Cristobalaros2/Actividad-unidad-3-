# Integración de IA — Prompts estructurados

Instrucciones redactadas para un agente de Inteligencia Artificial, según los
objetivos de la actividad "Huellas Sanas".

---

## Prompt 1: Generar el código HTML/CSS responsivo del formulario de ingreso y la tabla de visualización

```
ROL: Eres un desarrollador frontend especializado en HTML5, CSS3 y diseño responsive.

CONTEXTO:
Estamos construyendo el sistema web de la clínica veterinaria "Huellas Sanas"
con Django. La interfaz será renderizada con plantillas Django (syntax {{ }} y {% %}).

OBJETIVO:
Generar el código HTML/CSS responsivo de dos vistas:
1. Formulario de ingreso de nuevos pacientes (mascotas).
2. Tabla de visualización del listado diario de citas.

REQUISITOS TÉCNICOS:
- Formulario: campos Nombre de la mascota, Especie, Raza y Nombre del dueño.
  Debe mostrar errores de validación por campo y usar token CSRF.
- Tabla: columnas Hora, Paciente, Especie/Raza, Dueño, Motivo de consulta,
  Estado (etiqueta de color: pendiente/atendida/cancelada) y Acciones
  (botones para atender o cancelar cada cita).
- Responsivo: en pantallas menores a 760px la tabla se convierte en tarjetas
  apiladas (cada celda muestra su etiqueta con data-label).
- Estética: paleta verde institucional, cabecera con menú de navegación
  (Citas del día / Registrar paciente / Admin Django), mensajes de éxito/error.
- Usar HTML semántico, accesible (labels asociados a inputs) y sin dependencias
  externas (sin Bootstrap ni jQuery).

FORMATO DE SALIDA:
Archivos completos: base.html, lista_citas.html, crear_mascota.html y estilos.css
compatibles con el motor de plantillas de Django.
```

---

## Prompt 2: Crear un script que genere datos ficticios de 20 pacientes y citas iniciales

```
ROL: Eres un desarrollador backend Python especializado en Django ORM.

CONTEXTO:
Proyecto Django "Huellas Sanas" (app: citas) con los modelos:
- Mascota(nombre, especie, raza, nombre_dueno)
- Cita(mascota FK, fecha, hora, motivo_consulta, estado[pendiente/atendida/cancelada])

OBJETIVO:
Crear un script Python (ej: generar_datos_ficticios.py) que genere datos
ficticios para validar el funcionamiento del sistema.

REQUISITOS TÉCNICOS:
- Generar exactamente 20 pacientes (mascotas) con nombres de mascotas y
  apellidos de dueños realistas, escritos SIN tildes ni caracteres especiales.
- Generar citas asociadas a esos pacientes:
  * Al menos 10 citas para el día de hoy (para probar el listado diario).
  * El resto distribuido en días pasados y futuros (rango -14 a +14 días).
  * Estados variados: mayoría pendiente, algunas atendidas y canceladas.
  * Horarios en franjas de 9:00 a 17:00 en intervalos de 30 minutos.
  * Motivos de consulta variados (vacunación, control de peso, etc.).
- Usar random.seed() para que los datos sean reproducibles.
- El script debe ser idempotente: no duplicar datos si ya existen en la BD.
- Configurar DJANGO_SETTINGS_MODULE y django.setup() antes de usar los modelos.
- Imprimir un resumen al finalizar (pacientes y citas creados/totales).

FORMATO DE SALIDA:
Un archivo .py ejecutable con: pipenv run python generar_datos_ficticios.py
```

---

## Prompt 3: Administrar las citas que se generaron mediante el Framework de Django

```
ROL: Eres un desarrollador backend senior en Python/Django.

CONTEXTO:
Sistema "Huellas Sanas" ya con datos ficticios cargados. El administrador de la
clínica necesita administrar las citas (cambiar su estado) usando el framework
Django, sin tocar la base de datos directamente.

OBJETIVO:
Implementar la administración de las citas generadas mediante Django, cubriendo
dos caminos oficiales del framework:

A) Vistas y rutas (para recepcionistas):
   - Vista de listado diario de citas (?fecha=YYYY-MM-DD, por defecto hoy) que
     muestre hora, mascota, dueño, motivo, estado y acciones.
   - Vista de formulario para registrar nuevos pacientes (ModelForm + CSRF).
   - Vista POST que actualice el estado de una cita (atender/cancelar/reabrir)
     y redirija al listado de su fecha conservando mensajes de feedback
     (django.contrib.messages).
   - URLs con include() en el proyecto y nombres reverse-ables.

B) Django Admin (para el director):
   - Modelos registrados con CRUD completo, list_filter por estado y fecha,
     búsqueda y date_hierarchy (ya implementado en citas/admin.py).

REQUISITOS TÉCNICOS:
- Usar ORM de Django (nunca SQL crudo).
- Validación de formularios con ModelForm.
- Protección CSRF en todos los POST.
- Códigos de estado correctos: redirect tras POST exitoso (patrón POST/redirect/GET).

FORMATO DE SALIDA:
Archivos forms.py, views.py, urls.py (app y proyecto) y plantillas asociadas,
con la estructura de carpetas citations/templates/.
```

---

*Nota: estos prompts fueron la especificación utilizada para generar el código
de vistas, rutas, plantillas y datos ficticios de esta unidad, mediante un
agente de Inteligencia Artificial.*
