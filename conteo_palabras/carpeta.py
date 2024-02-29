import os 
from conteo_palabras.csv import Csv
from conteo_palabras.json import Json
from conteo_palabras.txt import Txt
from conteo_palabras.xml import Xml

class Carpeta:

    def __init__(self, ruta:str) -> None:
        self.ruta = ruta
        self.archivos = []
        self.crearArchivos()

    #metodo que verifica si la carpeta existe
    def verificarCarpeta(self):
        if not os.path.isdir(self.ruta):
            print(f'Mensaje indicado que no se encuentra en la carpeta indicada')
            return False
        return True

    #metodo que verifica si la carpeta contiene archivos de texto
    def crearArchivos(self):
        if self.verificarCarpeta():
            for nombreArc in os.listdir(self.ruta):
                rutaCompleta = os.path.isfile(f'{self.ruta}/{nombreArc}')
                # Verificamos si es un archivo de tipo json, csv, txt o xml
                if rutaCompleta:
                    extension = nombreArc.split('.')[-1].lower()
                    if extension == 'json':
                        self.archivos.append(Json(f'{self.ruta}/{nombreArc}', nombreArc))
                    if extension == 'csv':
                        self.archivos.append(Csv(f'{self.ruta}/{nombreArc}', nombreArc))
                    if extension == 'txt':
                        self.archivos.append(Txt(f'{self.ruta}/{nombreArc}', nombreArc))
                    if extension == 'xml':
                        self.archivos.append(Xml(f'{self.ruta}/{nombreArc}', nombreArc))
                    if extension not in ['json', 'csv', 'txt', 'xml']:
                        print(f'Mensaje indicando que no se encontraron archivos de texto en la carpeta')

    #metodo que busca la palabra en los archivos de la carpeta
    def palabraBusqueda(self, palabra: str):
        total = 0
        for archivo in self.archivos:
            cantidad = archivo.contarPalabras(palabra)
            total += cantidad
            print(f'Solo el archivo {archivo._nombreArc} tiene {cantidad} veces la palabra {palabra}')

        if self.archivos:
            print(f'En total {total} de veces que se encuentra la palabra {palabra} en los archivos de la carpeta')