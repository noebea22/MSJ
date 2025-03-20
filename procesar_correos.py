import sqlite3
import os
import re  
from docx import Document
from striprtf.striprtf import rtf_to_text

DB_NAME = "correos.db"

def crear_tablas():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS correos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            promotor TEXT,
            asunto TEXT,
            ejecutivo TEXT,
            informativo TEXT,
            UNIQUE(promotor, asunto)
        )
        """)
        conn.commit()

def extraer_texto_docx(ruta_archivo):
    """Extrae el texto de un archivo DOCX"""
    doc = Document(ruta_archivo)
    return "\n".join([p.text for p in doc.paragraphs])

def extraer_texto_rtf(ruta_archivo):
    """Extrae el texto de un archivo RTF"""
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as file:
            return rtf_to_text(file.read())
    except UnicodeDecodeError:
        print(f"⚠ Error con UTF-8 en {ruta_archivo}, probando otra codificación...")
        with open(ruta_archivo, "r", encoding="windows-1252") as file:
            return rtf_to_text(file.read())

def extraer_datos_correo(texto):
    """Extrae los campos promotor, asunto, ejecutivo e informativo del correo"""
    
    # Extraer Promotor (formato ALGO-XX)
    promotor = re.search(r"Promotor:\s*([A-Z]+-[A-Z]{2})", texto)
    promotor = promotor.group(1) if promotor else ""

    # Extraer Asunto (formato Número + Letra + "GHO" + DDhhmm + MES + aa)
    asunto = re.search(r"Asunto:\s*(\d{4} [A-Z] GHO \d{6} [A-Z]{3} \d{2})", texto)
    asunto = asunto.group(1) if asunto else ""

    # Extraer Ejecutivo(s) (formato ALGO-XX, separado por coma o barra)
    ejecutivo = re.findall(r"Ejecutivo:\s*([A-Z]+-[A-Z]{2})(?:[,/]\s*[A-Z]+-[A-Z]{2})*", texto)
    ejecutivo = ', '.join(ejecutivo) if ejecutivo else ""

    # Extraer Informativo(s) (formato ALGO-XX, separado por coma o barra)
    informativo = re.findall(r"Informativo:\s*([A-Z]+-[A-Z]{2})(?:[,/]\s*[A-Z]+-[A-Z]{2})*", texto)
    informativo = ', '.join(informativo) if informativo else ""

    return promotor, asunto, ejecutivo, informativo

def agregar_correo(conn, promotor, asunto, ejecutivo, informativo):
    """Agrega un correo a la base de datos, evitando duplicados"""
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR IGNORE INTO correos (promotor, asunto, ejecutivo, informativo)
        VALUES (?, ?, ?, ?)
    """, (promotor, asunto, ejecutivo, informativo))
    conn.commit()
    return cursor.lastrowid

def procesar_archivo(ruta_archivo):
    """Determina el tipo de archivo, extrae datos y los guarda en la BD evitando duplicados"""
    if ruta_archivo.startswith("~$"):
        print(f"🔹 Ignorando archivo temporal: {ruta_archivo}")
        return

    extension = os.path.splitext(ruta_archivo)[1].lower()

    if extension == ".docx":
        try:
            texto = extraer_texto_docx(ruta_archivo)
        except Exception as e:
            print(f"⚠ Error al procesar {ruta_archivo}: {e}")
            return
    elif extension == ".rtf":
        texto = extraer_texto_rtf(ruta_archivo)
    else:
        print(f"⚠ Formato no soportado: {ruta_archivo}")
        return

    promotor, asunto, ejecutivo, informativo = extraer_datos_correo(texto)

    if not asunto:
        print(f"⚠ Asunto inválido en {ruta_archivo}")
        return

    try:
        with sqlite3.connect(DB_NAME) as conn:
            correo_id = agregar_correo(conn, promotor, asunto, ejecutivo, informativo)
            if correo_id:
                print(f"✅ Correo agregado con éxito: {promotor} - {asunto}")
            else:
                print(f"⚠ Correo duplicado: {promotor} - {asunto}")
    except Exception as e:
        print(f"❌ Error procesando {ruta_archivo}: {e}")

def procesar_carpeta(carpeta_base):
    """Procesa todos los archivos DOCX y RTF en la carpeta"""
    for raiz, _, archivos in os.walk(carpeta_base):
        for archivo in archivos:
            ruta_completa = os.path.join(raiz, archivo)
            if archivo.endswith((".docx", ".rtf")):
                procesar_archivo(ruta_completa)

# Crear las tablas necesarias en la base de datos
crear_tablas()

# Procesar todos los archivos en la carpeta "carpeta_de_correos"
procesar_carpeta("carpeta_de_correos")
