# print: Es una función en Python que nos permite mostrar información en la consola.
# Podemos utilizarla para imprimir mensajes, valores de variables u otros datos que queramos
# visualizar durante la ejecución del programa.

# input: Es una función en Python que nos permite recibir datos de entrada desde el usuario.
# Al utilizarla, el programa se detiene y espera a que el usuario ingrese un valor.
# Luego, ese valor puede ser almacenado en una variable para su posterior uso en el programa.

# Librería: En Python, una librería es un conjunto de funciones, clases y variables predefinidas
# que se agrupan para realizar tareas específicas. Estas librerías amplían las capacidades del
# lenguaje y nos permiten utilizar funcionalidades adicionales sin tener que implementarlas desde
# cero. Podemos importar una librería en nuestro programa para acceder a sus funcionalidades y
# utilizarlas en nuestro código.

# Extensión .py: En Python, la extensión de archivo .py se utiliza para identificar los archivos
# de código fuente escritos en Python. Estos archivos contienen el código que será interpretado 
# y ejecutado por el intérprete de Python. Al guardar nuestros programas en archivos con extensión
# .py, podemos ejecutarlos y compartirlos con otros desarrolladores.

import sys


print(f"Buenos días {sys.argv[1]}")

>>> py saludo.py Juan
→  Buenos días Juan

