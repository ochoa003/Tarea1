import xml.etree.ElementTree as ET
from .archivo import Archivo

class Xml(Archivo):

    def __init__(self, rutaArc: str, nombreArc: str):
        super().__init__(rutaArc, nombreArc)

    #Se lee el archivo xml y se guarda en un diccionario
    def leer(self):
        try:
          arbol = ET.parse(self._ruta)
          raiz = arbol.getroot()
          datos = {}
          for elemento in raiz:
            datos[elemento.tag] = elemento.text
            self.texto = str(datos)
        except FileNotFoundError:
            print(f"El archivo '{self._nombre}' no fue encontrado.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")
    
    def contarPalabras(self, palabra:str):
        totalPalabras = super().contarPalabras(palabra)
        return len(totalPalabras)