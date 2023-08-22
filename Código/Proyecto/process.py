# autor: Junior Castillo - jicastilloh@unah.hn
# version: 0.0.4

import re, subprocess as sp, sys

ruta_archivoURLs = sys.argv[1]

# Leer la cantidad de archivos
cantidad_archivos = 0
with open(f'{ruta_archivoURLs}', 'r') as archivoURLs:
    enlaces = archivoURLs.read().split() # Creo una lista que contega cada línea del archivo de URLs
    cantidad_archivos = (len(enlaces)) # Extraigo el número de enlaces
archivoURLs.close()

# Función para obtener las etiquetas de un archivo HTML y las ocurrencias de cada etiqueta
def extraer_etiquetas(nombre_archivo):
    etiquetas_contadas = {}
    with open(nombre_archivo, 'r') as archivo_html:
        lectura = archivo_html.read()
        # Encontrando todas las etiquetas HTML en el archivo
        lista_de_etiquetas = re.findall(r'<([a-z][a-z0-9]*)[^>]*', lectura)
        # Contando las etiquetas encontradas
        for etiqueta in lista_de_etiquetas:
            etiquetas_contadas[etiqueta] = etiquetas_contadas.get(etiqueta, 0) + 1
    return etiquetas_contadas

# Guardando los datos de las etiquetas
lista_diccionarios_archivos = list(map(
    lambda i: extraer_etiquetas(f'./HTML_Descargadas/url{i+1}.html'), 
    range(cantidad_archivos))
    ) # En esta lista, cada elementos será un diccionario que contiene las etiquetas de cada archivo con sus ocurrencias

datos = {} # Variable que va a contener todas las etiquetas con sus ocurrencias
for diccionario in lista_diccionarios_archivos: # Recorro cada diccionario de la lista 'lista_diccionarios_archivos'
    for etiqueta, ocurrencias in diccionario.items(): # Recorro la 'llave' y 'valor' de cada diccioanrio
        datos[etiqueta] = datos.get(etiqueta, 0) + ocurrencias # Guardamos la cantidad total de las etiquetas

def convertir_datos(diccionario):
    informacion = ""
    for etiqueta, ocurrencias in diccionario.items(): 
        informacion += f'{etiqueta},{ocurrencias}\n'
    return informacion.strip()

texto = convertir_datos(datos)        

# Ejecuto el archivo 'solverL.lisp' y le paso la variable con la información que tiene que procesar como parámetro.
sp.run(["sbcl", "--script", "solverL.lisp", texto])