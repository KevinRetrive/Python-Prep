# Para definir una función en Python se utiliza la palabra reservada def, a continuación viene el nombre
# de la función que es el que se utilizará luego para invocarla. Después del nombre hay que incluir los
# paréntesis y dentro de ellos una lista opcional de parámetros. Finalmente colocamos  dos puntos. 
# Luego de  los dos puntos se incluye el cuerpo de la función, con una sangría.En el cuerpo de la función
# van el conjunto de instrucciones que se encapsulan en dicha función.  En último lugar y de manera
# opcional, se añade la instrucción con la palabra reservada return para devolver un resultado.
# Ej:

def saludar(num):
    if num > 0:
        print("Welcome")
    else:
        print("Good bye")
    return f"El n° imputado fue: {num}"

saludar(5)

# Límites al declarar funciones:

# Los nombres no pueden comenzar con dígitos
# No se puede utilizar una palabra reservada
# Las variables deben tener diferentes nombres
# Los nombres de las funciones deben ser descriptivas de lo que hacen las funciones
# Los parámetros pueden tener valores por defecto
# Una función puede devolver ninguno, uno o más de un valor, y de diferentes tipos de datos

# Variables locales y globales

# Una variable declarada fuera de cualquier función o clase tiene un alcance GLOBAL. 
# Esto significa que puede ser accedida desde cualquier lugar del programa, 
# incluyendo dentro de funciones y clases.

# Una variable declarada dentro de una función o clase tiene un alcance LOCAL. 
# Esto significa que solo puede ser accedida dentro de esa función o clase, y no fuera de ella.

def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

def saludar(nombre, saludo="Hola"):
    print(saludo + ", " + nombre)

def sumar(sumando1, sumando2):
    resultado = sumando1 + sumando2
    return resultado