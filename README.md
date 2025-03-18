# Proyecto de Organización de Mensajes Internos

## Descripción

Este sistema permite organizar los mensajes internos de una organización extrayéndolos desde archivos en formatos `.doc`, `.rtf` y `.docx`. La información se almacena en una base de datos SQLite3, aunque en el futuro podría migrarse a otro motor de base de datos.

Cada mensaje es identificado de manera única por un `promotor` y una cadena de caracteres que sigue la estructura:

```
Número + Letra + "GHO" + DDhhmm + MES + aa
```

Ejemplo:

```
0554 R GHO 161550 MAR 25
```

Además, cada mensaje cuenta con direcciones `ejecutivo` (destinatarios principales) y `informativo` (destinatarios en copia opcional). El cuerpo del mensaje se encuentra debajo de estos campos.

## Requerimientos

### Requerimientos de Software

- Python 3.x
- SQLite3
- Librerías de Python:
  - `sqlite3`
  - `os`
  - `re`
  - `python-docx` (para leer archivos `.docx`)
  - `striprtf` (para leer archivos `.rtf`)

Para instalar las librerías necesarias, ejecutar:

```sh
pip install python-docx striprtf
```

### Estructura del Proyecto

```
proyecto/
│-- main.py               # Código principal
│-- correos.db            # Base de datos SQLite3
│-- carpeta_de_correos/   # Carpeta con archivos a procesar
│-- README.md             # Documentación
```

## Funcionamiento

1. **Creación de la base de datos:** Se crea la base de datos `correos.db` con una tabla `correos` si no existe.
2. **Procesamiento de archivos:** Se recorren los archivos en `carpeta_de_correos/`, extrayendo los datos relevantes.
3. **Almacenamiento de datos:** Los mensajes se insertan en la base de datos evitando duplicados.
4. **Identificación de mensajes:** Se identifican con `promotor` y `asunto`.
5. **Direcciones:** Se extraen `ejecutivo` y `informativo`.

## Uso

Ejecutar el script principal:

```sh
python main.py
```

Esto procesará todos los archivos en `carpeta_de_correos/` e insertará los datos en la base de datos.

## Posibles Mejoras

- Soporte para otros formatos de archivos.
- Implementación de una interfaz gráfica.
- Migración a una base de datos más robusta.
