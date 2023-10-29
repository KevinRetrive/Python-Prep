# Recuerda importar la librería os al comienzo de tu programa utilizando import os para poder 
# utilizar estas funciones. Si tienes alguna otra pregunta, no dudes en hacerla.

import os

# Crear una carpeta nueva:
# Para crear una carpeta nueva en Python, utilizamos el método makedirs() de la librería os.
# Simplemente especificamos la ruta de la carpeta que queremos crear y este método se encarga
# de crearla en el sistema de archivos.

# os.makedirs("Notas teóricas//M10//Cree_esta_carpeta_con_OS")

# Lista el contenido de una carpeta:
# Para listar el contenido de una carpeta en Python, utilizamos el método listdir() de la
# librería os. Este método nos devuelve una lista con los nombres de los archivos y subdirectorios
# que se encuentran en la carpeta especificada.

# os.listdir("") y dentro de las comillas ponemos la ruta

# Mostrar el directorio de trabajo:
# Para mostrar el directorio de trabajo actual en Python, utilizamos el método getcwd()
# de la librería os. Este método devuelve una cadena de texto que representa la ruta absoluta
# del directorio actual.

os.getcwd() # cwd "current work directory"

# Mostrar el tamaño en bytes de un archivo pasado como parámetro:
# Para obtener el tamaño en bytes de un archivo en Python, utilizamos el método getsize()
# de la librería os.path. Simplemente especificamos la ruta del archivo y este método nos 
# devuelve el tamaño en bytes.

os.path.getsize("Interactuar_sistema_archivos.py")

# Verificar si el parámetro pasado a la función es un archivo:
# Para verificar si un parámetro es un archivo en Python, utilizamos el método isfile() de la
# librería os.path. Este método devuelve un valor booleano (True o False) que indica si el
# parámetro es un archivo válido.

# Verificar si el parámetro pasado a la función es una carpeta:
# Para verificar si un parámetro es una carpeta en Python, utilizamos el método isdir() de la
# librería os.path. Este método devuelve un valor booleano que indica si el parámetro es una 
# carpeta válida.

# Cambiar directorio/carpeta:
# Para cambiar el directorio o carpeta actual en Python, utilizamos el método chdir() de la 
# librería os. Simplemente especificamos la ruta de la nueva carpeta a la que queremos cambiar
# y este método actualiza el directorio actual.

# Renombrar un archivo:
# Para renombrar un archivo en Python, utilizamos el método rename() de la librería os. 
# Especificamos la ruta y el nombre actual del archivo, junto con el nuevo nombre que queremos
# asignarle.

# Eliminar un archivo:
# Para eliminar un archivo en Python, utilizamos el método remove() de la librería os.
# Simplemente especificamos la ruta del archivo que queremos eliminar y este método se encarga
# de borrarlo del sistema de archivos.

# Eliminar una carpeta:
# Para eliminar una carpeta en Python, utilizamos el método rmdir() de la librería os. 
# Especificamos la ruta de la carpeta que queremos eliminar y este método se encarga de borrarla,
# siempre y cuando esté vacía.



