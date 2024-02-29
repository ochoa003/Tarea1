import re
from abc import ABC, abstractmethod

class Archivo(ABC):

    def __init__(self, rutaArc: str, nombreArc: str):
        self._rutaArc = rutaArc
        self._nombreArc = nombreArc
        self.texto = ''

    #se cuenta la cantidad de veces que aparece la palabra en el texto haciendolo revisando que se encuentre entre espacios
    def contarPalabras(self, palabra:str):
        self.leer()
        totalPalabras = re.findall(r'\b' + re.escape(palabra) + r'\b', self.texto, flags=re.IGNORECASE)
        return totalPalabras

    @abstractmethod
    def leer(self, palabra:str):
        pass
