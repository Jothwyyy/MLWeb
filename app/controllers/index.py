import web
import csv
import io

import pandas as pd

render = web.template.render('app/views', base='template')

class Index:

    def __init__(self):
        pass

    def info(self):
        ruta_archivo = f"static/csv/archivo.csv"
        df = pd.read_csv(ruta_archivo)

        informacion = {
            "shape": df.shape,
            "dtype": df.dtypes
        }
        return informacion

    def estadistica_descriptiva(self):
        ruta_archivo = f"static/csv/archivo.csv"

        df = pd.read_csv(ruta_archivo)

        return {
            "cantidad_filas": len(df)

        }
 

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

        ruta_archivo = f"static/csv/archivo.csv"
        with open(ruta_archivo, mode="w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(filas)

        # Llamamos al metodo info que utiliza pandas para analizar el csv
        csv_info = self.info()

        return csv_info