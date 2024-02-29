import json
from .archivo import Archivo

class Json(Archivo):

    def __init__(self, rutaArc: str, nombreArc: str):
        super().__init__(rutaArc, nombreArc)
        
    #Se lee el archivo json y se guarda en un diccionario
    def leer(self):
        try:
          with open(self._rutaArc, "r") as archivo:
            datos = json.load(archivo)
            self.texto = str(datos) 
        except FileNotFoundError:
           print(f"El archivo '{self._nombreArc}' no fue encontrado.")
        except json.JSONDecodeError as e:
         print(f"Error al decodificar el archivo JSON: {e}")
        except Exception as e:
          print(f"Ocurrió un error: {e}")

    def contarPalabras(self, palabra:str):
        totalPalabras = super().contarPalabras(palabra)
        return len(totalPalabras)