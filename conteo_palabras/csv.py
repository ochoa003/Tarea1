import csv
from .archivo import Archivo

class Csv(Archivo):

    def __init__(self, rutaArc: str, nombreArc: str):
        super().__init__(rutaArc, nombreArc)

    #Se lee el archivo csv y se guarda en un diccionario
    def leer(self):
        try:
          with open(self._rutaArc, "r", newline="") as archivo:
              lector_csv = csv.DictReader(archivo)
              datos = []
              for fila in lector_csv:
                  datos.append(dict(fila))
                  self.texto = str(datos)

        except FileNotFoundError:
              print(f"El archivo '{self._nombreArc}' no fue encontrado.")

        except Exception as e:
              print(f"Ocurrió un error: {e}")
    
    def contarPalabras(self, palabra:str):
         totalPalabras = super().contarPalabras(palabra)
         return len(totalPalabras)