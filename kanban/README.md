# 📋 Planificación y Control GM

**Planificación y Control GM** es una aplicación web ligera en **HTML, CSS y JavaScript puro** que permite gestionar tareas a través de un **tablero Kanban** o una **vista de calendario**.  
Ideal para el seguimiento de proyectos, tareas o actividades del equipo. Este programa puede ser compartido en redes administradas donde no se cuentan con permisos de administrador.

---

## 🚀 Características

- ✅ Tablero **Kanban** con tres columnas: _Planificada_, _En progreso_ y _Finalizada_.
- 📅 Vista de **Calendario mensual** para visualizar el inicio y fin de las tareas.
- ➕ Agregar nuevas tareas con título, descripción, fechas y estado.
- 🔍 Filtro de búsqueda por título o descripción.
- 📤 **Exportación de tareas a CSV** para análisis o respaldo externo.
- ⚠️ Indicador visual de **tareas vencidas** (en rojo).
- 🧾 **Resumen de tareas** por estado.

---

## 🧱 Tecnologías utilizadas

- HTML5
- CSS3 (estilizado básico con Flexbox)
- JavaScript puro (sin frameworks)

---

## 🧪 Cómo usar

1. **Abrir el archivo:** Solo necesitas abrir el archivo `.html` en un navegador moderno (Chrome, Firefox, Edge, etc).
2. **Agregar tareas:** Usa la barra superior para ingresar título, descripción, fecha de inicio/fin y estado.
3. **Navegar entre vistas:**
   - Usa el botón **"Alternar Vista"** para cambiar entre el tablero Kanban y el calendario.
   - En la vista de calendario, puedes cambiar de mes con los botones **"Anterior"** y **"Siguiente"**.
4. **Filtrar tareas:** Usa el campo de búsqueda para encontrar tareas rápidamente.
5. **Exportar tareas:** Presiona **"Exportar CSV"** para descargar el listado de tareas.

---

## 📁 Estructura del archivo

Todo el código está contenido en un solo archivo `.html`, que incluye:

- `<style>`: Estilos internos.
- `<script>`: Lógica de manejo de tareas y renderizado.

La interfaz se estructura en:

- `kanban-board`: Vista estilo tablero Kanban.
- `calendarView`: Calendario mensual dinámico.

---

## 📝 Notas

- No se requiere conexión a internet ni instalación adicional.
- Los datos se almacenan solo en memoria (no hay persistencia local).
- Puedes modificar la lista inicial de tareas dentro del arreglo `tareas[]` en el script.

---

## ✨ Ejemplo de uso

Al abrir el archivo, verás un tablero con tareas predefinidas. Puedes agregar nuevas tareas, filtrarlas o alternar al calendario para visualizarlas por fecha.

---

## 📦 Exportación

La funcionalidad **"Exportar CSV"** genera un archivo con los siguientes campos:

- Título
- Descripción
- Fecha de inicio
- Fecha de fin
- Estado

---

## 🛠️ Actualización de datos

Este proyecto incluye una herramienta web que permite actualizar fácilmente el contenido del **tablero HTML** con nuevas tareas provenientes de un archivo `.csv`.

### ¿Para qué sirve?

Permite reemplazar las tareas existentes en un archivo `tablero.html` con nuevas tareas listadas en un archivo `tareas.csv`, sin necesidad de editar manualmente el HTML.  
Ideal si gestionas las tareas desde una hoja de cálculo o sistema externo.

### Cómo usarlo

1. Abre el archivo `generador.html` (incluido en el proyecto).
2. Carga los archivos:
   - 📄 **Cargar tablero.html:** selecciona el archivo HTML original.
   - 📑 **Cargar tareas.csv:** selecciona el archivo CSV con las nuevas tareas.
3. Haz clic en **🎯 Generar HTML Final**.
4. Descarga el nuevo archivo haciendo clic en **⬇️ Descargar HTML generado**.

### Formato del archivo CSV

El archivo `.csv` debe tener la siguiente estructura (primera fila como encabezado):

````csv
"id","título","estado","descripcion","inicio","fin"

Ejemplo de contenido:

"1","Preparar informe","en progreso","Redactar informe mensual","2025-04-01","2025-04-05"
"2","Revisión","pendiente","Revisar documento legal","2025-04-06","2025-04-07"

### 🔍 ¿Qué hace internamente?

Este generador automatiza el proceso de actualización del tablero HTML con los datos del archivo CSV. Internamente realiza los siguientes pasos:

1. **Carga el contenido de `tablero.html`.**
2. **Lee y convierte los datos del archivo `tareas.csv`** en un arreglo de objetos JavaScript utilizando los encabezados como claves.
3. **Reemplaza automáticamente** la línea original del archivo HTML que contiene las tareas:

   ```js
   let tareas = [...];


🛠️ Futuras mejoras (sugeridas)

TBD

📄 Licencia
Este proyecto se proporciona como base de uso libre para fines personales, educativos o profesionales. Puedes modificarlo según tus necesidades.
````
