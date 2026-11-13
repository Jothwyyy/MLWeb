import web
import csv
import io

render = web.template.render('app/views', base='template')

class Index:

    def __init__(self):
        pass

    def GET(self):
        return render.index()

    def POST(self):
        form = web.input(inp_file={})

        if not 'inp_file' in form:
            return "<h1>No se puede procesar el archivo</h1>"

        # Obtener el archivo
        archivo = form.get("inp_file")
        
        # Obtener el nombre del archivo
        nombre_csv = archivo.filename 

        contenido_bytes = archivo.file.read()
        contenido_texto = contenido_bytes.decode("utf-8")

        leer_csv = csv.reader(io.StringIO(contenido_texto))

        filas = list(leer_csv)

        respuesta = f"Archivo {nombre_csv} recibido. filas: {len(filas)}"

        ruta_archivo = f"static/csv/{nombre_csv}"
        with open(ruta_archivo, mode="w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(filas)

        return respuesta