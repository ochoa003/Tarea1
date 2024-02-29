from .archivo import Archivo

class Txt(Archivo):

    def __init__(self, rutaArc: str, nombreArc: str):
        super().__init__(rutaArc, nombreArc)

    #Se lee el archivo txt y se guarda en una variable
    def leer(self):
        try:
            with open(self._rutaArc, "r") as archivo:
                 contenido = archivo.read()
                 self.texto = contenido
                 
        except FileNotFoundError:
            print(f"El archivo '{self._nombreArc}' no fue encontrado.")

        except Exception as e:
            print(f"Ocurrió un error: {e}")

    def contarPalabras(self, palabra:str):
         totalPalabras = super().contarPalabras(palabra)
         return len(totalPalabras)