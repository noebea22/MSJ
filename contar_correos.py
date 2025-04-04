import sqlite3

DB_NAME = "correos.db"


def contar_correos():
    """Consulta la cantidad de correos almacenados en la base de datos y muestra hasta 3 registros."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        
        # Contar total de correos
        cursor.execute("SELECT COUNT(*) FROM correos")
        cantidad = cursor.fetchone()[0]
        print(f"📩 Total de correos en la base de datos: {cantidad}\n")
        
        if cantidad > 0:
            # Seleccionar hasta 3 correos para mostrar
            cursor.execute("SELECT promotor, asunto, ejecutivo, informativo, cuerpo FROM correos LIMIT 3")
            correos = cursor.fetchall()
            
            print("📜 Mostrando hasta 3 correos:")
            for idx, (promotor, asunto, ejecutivo, informativo, cuerpo) in enumerate(correos, 1):
                print(f"\n📌 Correo {idx}:")
                print(f"   Promotor: {promotor}")
                print(f"   Asunto: {asunto}")
                print(f"   Ejecutivo: {ejecutivo}")
                print(f"   Informativo: {informativo}")
                print(f"   Cuerpo: {cuerpo}\n")

if __name__ == "__main__":
    contar_correos()
