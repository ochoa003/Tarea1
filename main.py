from conteo_palabras.carpeta import Carpeta

print('PRUEBA 1')
carpeta1 = Carpeta('./pruebas1')
carpeta1.palabraBusqueda('arar')

print('PRUEBA 2')
carpeta2 = Carpeta('./pruebas2')
carpeta2.palabraBusqueda('foto')

print('PRUEBA 3')
carpeta3 = Carpeta('./incorrecta')
carpeta3.palabraBusqueda('ejemplo')

print('PRUEBA 4')
carpeta1 = Carpeta('./pruebas3')
carpeta1.palabraBusqueda('arar')