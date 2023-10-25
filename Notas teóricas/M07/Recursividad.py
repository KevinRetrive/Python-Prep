# La recursividad como técnica de programación que permite definir funciones que se llaman a sí mismas
# dentro de su propio cuerpo. Ej:

# La función help() es una función incorporada en Python que se utiliza para obtener información
# detallada sobre los módulos, funciones, clases, métodos, palabras clave y cualquier otro objeto
# de Python. Al utilizar la función help() en un objeto o módulo, se muestra una descripción detallada
# de su funcionalidad, argumentos y otros detalles útiles. Esta función es especialmente útil
# para explorar y comprender la funcionalidad de un objeto en Python.


def factorial(numero):
    '''
    Calcula el factorial de un número
    '''
    if (numero > 1):
        numero = numero * factorial(numero - 1)
    return numero

help(factorial)