from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
import sqlite3

app = FastAPI()
DB_NAME = "correos.db"

# Página de inicio
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head><title>Buscar Correos</title></head>
        <body>
            <h2>Buscar Correos por Asunto</h2>
            <form action="/buscar" method="get">
                <input type="text" name="asunto" placeholder="Ingrese parte del asunto">
                <button type="submit">Buscar</button>
            </form>
        </body>
    </html>
    """

# Página para buscar correos
@app.get("/buscar", response_class=HTMLResponse)
def buscar_correos(asunto: str = Query(..., title="Asunto")):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT remitente, destinatarios, fecha_envio, asunto, cuerpo FROM correos WHERE asunto LIKE ?", ('%' + asunto + '%',))
        correos = cursor.fetchall()

    if not correos:
        return "<h3>No se encontraron correos con ese asunto.</h3>"

    html = "<h2>Resultados de la búsqueda</h2><hr>"
    for correo in correos:
        remitente, destinatarios, fecha_envio, asunto, cuerpo = correo
        html += f"""
        <h3>{asunto}</h3>
        <p><b>De:</b> {remitente}</p>
        <p><b>Para:</b> {destinatarios}</p>
        <p><b>Fecha:</b> {fecha_envio}</p>
        <p><b>Cuerpo:</b></p><pre>{cuerpo}</pre>
        <hr>
        """
    
    return HTMLResponse(content=html)

# Iniciar el servidor con uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
