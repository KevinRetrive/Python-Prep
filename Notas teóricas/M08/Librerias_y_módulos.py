# En Python, un módulo es un archivo que contiene código Python reutilizable que puede ser importado y
# utilizado en otros programas.

# Por otro lado, una librería o biblioteca es un conjunto de módulos que proporcionan una funcionalidad
# específica. Las bibliotecas suelen estar organizadas en un directorio que contiene varios archivos de
# módulo y se utilizan juntos para proporcionar una funcionalidad más compleja.

# Ej: Biblioteca math de PY
import math
x=16
raiz2=math.sqrt(x)
print(raiz2)
print("-----------------------------------")

# O creamos un archivo.py y lo llamamos con el nombre que lo creamos con la siguiente linea:

# Para sólo traer una parte específica del módulo:
# from #nombrearchivo.py import #funcion_o_metodo_a_usar

# Para traer todo el contenido del módulo:
# from #nombrearchivo.py import *
# Con el asterisco le indicamos que traemos todo


# sys.path es una lista en Python que contiene las rutas de búsqueda de módulos. 
# Cuando importas un módulo en Python, el intérprete busca ese módulo en los directorios incluidos
# en sys.path. Estos directorios pueden incluir la ubicación del script actual, los directorios de
# la biblioteca estándar de Python y cualquier otro directorio personalizado que hayas agregado.

# La modificación de sys.path te permite controlar qué directorios se consideran al buscar módulos.
# Puedes agregar o eliminar directorios según tus necesidades, lo que resulta útil cuando trabajas
# con módulos personalizados o estructuras de carpetas no convencionales. Sin embargo, debes tener
# cuidado al modificar sys.path, ya que puede afectar el correcto funcionamiento de tu programa si
# se realizan cambios incorrectos.

import sys
# sys.path.append(r"/ruta/de/acceso/al\modulo")
print(sys.path)

# as() y dir()

# En Python, puedes usar la palabra clave "as" para asignar un alias a un objeto o módulo. 
# Por ejemplo, puedes importar un módulo y darle un nombre más corto usando "as". 
# Por ejemplo: import math as m asigna el alias "m" al módulo "math", lo que te permite acceder a
# sus funciones utilizando m.funcion() en lugar de math.funcion().

# Ej:
import math as m
y=25
raiz_cua=m.sqrt(y)
print(raiz_cua)
print("-----------------------------------")

# Es importante notar que los módulos solamente son cargados una vez. Es decir, no importa el número
# de veces que llamemos a import mimodulo, que sólo se importará una vez. Si queremos que el módulo
# sea recargado, tenemos que ser explícitos, haciendo uso de reload. Ej:

import POO
import importlib
importlib.reload(POO)
importlib.reload(POO)
print("-----------------------------------")


# Dependiendo de la situación, puede ser importante especificar que únicamente queremos que se ejecute
# el código si el módulo es el main. Con la siguiente modificación, si hacemos import modulo desde otro
# módulo, este fragmento ya no se ejecutará al ser el módulo main otro. Ej:

# modulo.py
def suma(a, b):
    return a + b
if (__name__ == '__main__'):
    c = suma(1, 2)
    print("La suma es:", c)
print("-----------------------------------")



# dir() en Python se utiliza para obtener una lista de los nombres existentes en el espacio de nombres
# actual. Puedes llamar a dir() sin argumentos para obtener los nombres definidos en el alcance global,
# o pasarlo un objeto como argumento para obtener los nombres disponibles en ese objeto. Esta función 
# es útil para explorar los atributos y métodos disponibles en un objeto determinado, ayudándote a
# entender qué funcionalidades ofrece y cómo interactuar con ellas.

# Ej:

lista=[1,2,3]
print(dir(lista)) 
# Nos muestra todas las funciones aplicables a un iterable tipo lista


# Forma de escribir en mi pc las rutas:
# import sys
# print(sys.path) con esto veo la ruta en la que estoy
# sys.path.insert(0,'c:/Users/Kevin/OneDrive/Escritorio/Python-Prep/M08_clasesyOOP/Archivo_punto_8.py')
