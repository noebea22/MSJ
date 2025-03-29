import sqlite3

DB_NAME = "correos.db"

def contar_correos():
    """Consulta la cantidad de correos almacenados en la base de datos."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM correos")
        cantidad = cursor.fetchone()[0]
        print(f"📩 Total de correos en la base de datos: {cantidad}")

if __name__ == "__main__":
    contar_correos()
