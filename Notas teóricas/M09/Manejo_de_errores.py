# ¿Cómo verificar calidad y funcionalidad del software?

# 2 métodos. Prueba de caja negra y de cristal.

# Caja negra:

# Las pruebas de caja negra son un enfoque de pruebas en el que se evalúa el funcionamiento de un sistema
# sin conocer su implementación interna. En otras palabras, se prueba el sistema desde una perspectiva
# externa, centrándose únicamente en las entradas INPUTS y salidas OUTPUTS esperadas, sin tener
# conocimiento detallado de cómo se procesan los datos o cómo se realizan las operaciones internas.

# Hay dos tipos de pruebas de caja negra --> Las unitarias y las de integración:

# Las de integración simulan un sistema completo, de varios componentes/unidades, verificando la integración.
# Las pruebas unitarias usan unidades de código pequeñas o aisladas, no se tiene en cuenta su integración
# a un sistema y busca el funcionamiento de c/unidad por sí sola.
# Ej de prueba unitaria:

import unittest

def suma(num_1,num_2):
        return num_1+num_2

class CajaNegraTest(unittest.TestCase):

    def test_suma_dos_positivos(self):
        num_1 = 10
        num_2 = 5

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, 15)

# .assertEqual() es un método de la clase TestCase de la librería unittest, que nos permite ver si 
# el resultado es el esperado (debemos ingresarlo tal y como es)

    def test_suma_dos_negativos(self):
        num_1 = -10
        num_2 = -7

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, -17)
        
unittest.main(argv=[""],verbosity=2,exit=False)
# argv se utiliza para proporcionar argumentos de línea de comando a la prueba, 
# ahora pasamos uno vacío que no tiene efecto en la prueba que realizamos.

# verbosity se usa para controlar la cantidad de información de depuración que se muestra durante 
# la ejecución, al indicarle 2 nos mostrará una línea de resumen para c/método de prueba 
# y una línea detallada para cada prueba que falle.

# exit se usa para indicar si se debe detener la ejecución tras realizar la prueba.
# exit = False sirve para evitar que la prueba se detenga después de la ejecución de la misma. 
# Es decir, no se puede ejecutar el archivo hasta terminar la prueba.

# Caja de cristal:

# Las pruebas de caja de cristal están diseñadas para probar todas las posibles vías de ejecución de un 
# programa, incluyendo todas las ramas de decisión, bucles, recursiones, y cualquier otra estructura que
# pueda influir en el flujo del programa.

# Para realizar estas pruebas, se asume que se comprende el funcionamiento del programa en detalle, 
# lo que permite una cobertura exhaustiva de todas las partes del código. Para realizar estas pruebas,
# se asume que se comprende el funcionamiento del programa en detalle, lo que permite una cobertura 
# exhaustiva de todas las partes del código. Ej:

def es_mayor_de_edad(edad):
    if edad>=18:
        return True
    else:
        return False

class PruebaDeCristalTest(unittest.TestCase):

    def test_es_mayor_de_edad(self):
        edad = 20

        resultado = es_mayor_de_edad(edad)

        self.assertEqual(resultado, True)

    def test_es_menor_de_edad(self):
        edad = 15

        resultado = es_mayor_de_edad(edad)

        self.assertEqual(resultado, False)

unittest.main(argv=[""],verbosity=2,exit=False)

# Forma de escribir en mi pc las rutas:
# import sys
# print(sys.path) con esto veo la ruta en la que estoy
# sys.path.insert(0,'c:/Users/Kevin/OneDrive/Escritorio/Python-Prep/M08_clasesyOOP/Archivo_punto_8.py')

