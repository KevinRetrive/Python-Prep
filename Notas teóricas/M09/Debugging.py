# La palabra "debugging" se refiere al proceso de encontrar y corregir errores en el código de programación.
# La palabra "debug" en inglés significa "depurar" o "eliminar errores".

# EXCEPCIONES
# Manejo de excepciones:

# Las excepciones de Python normalmente se relacionan con errores de semántica. Nosotros también podemos
# crear nuestras propias excepciones, ya que cuando una excepción no se maneja (unhandled exception),
# el programa termina en error.

# Las excepciones pueden ser causadas por diferentes factores, como errores de sintaxis, 
# intentos de acceder a elementos inexistentes, divisiones entre cero o cualquier otra condición imprevista.
# Cuando se produce una excepción, el programa se detiene y busca un bloque de código que pueda manejarla.

# Las excepciones se manejan con los keywords: try, except, finally. 
# Se pueden utilizar también para ramificar programas.
# Para crear tu propia excepción, se usa el keyword: raise.

# Ej:

def multiplica_por_dos(lista):
    lista_multiplicada = []
    for num in lista:
        lista_multiplicada.append(num * 2)
    return lista_multiplicada

def divide_elementos_de_lista(lista, divisor):
    '''
    Cada elemento de una lista es dividida por un divisor definido.
    En caso de error de tipo ZeroDivisionError que
    significa error al dividir en cero
    la función devuelve la lista inicial
    '''

    try: # Se intenta realizar lo siguiente
        return [i / divisor for i in lista]

    except ZeroDivisionError as e: # Exceptuando esta situación
        print(e)
        return lista

lista=list(range(10))
divisor=0
print(divide_elementos_de_lista(lista,divisor))
# Como le añadí una excepción me aclara que es una división por cero y que no se puede, 
# y por lo tanto me devuelve la lista original como le indicamos.

# Ej2:
def dividir(num1, num2):
    try:
        resultado = num1 / num2
        return resultado
    except ZeroDivisionError:
        print("No se puede dividir por cero.")
        return None

# Ej3:
try:
    with open("archivo.txt", "r") as f:
        contenido = f.read()
except FileNotFoundError: # En otro ejemplo, KeyError es cuando busco una key de un diccionario y no está.
    print("El archivo no existe.")


# AFIRMACIONES

# Técnica de programación defensiva para verificar si una condición se cumple o no.

# La sintaxis es la siguiente:
#assert #condición, #mensaje_de_error

# La condición se trabaja con una salida del tipo booleano, es decir, True or False.
# Si la condición es False, se levanta una excepción con el mensaje_de_error que le indiqué.
# Ej:

def primera_letra(lista_de_palabras):
  primeras_letras = []

  for palabra in lista_de_palabras:
    assert type(palabra) == str, f'{palabra} no es str'
    assert len(palabra) > 0, 'No se permiten str vacíos'

    primeras_letras.append(palabra[0])
  return primeras_letras

palabras=["Hola","Mundo",42]
resultado=primera_letra(palabras)
print(resultado) # Me dice AssertionError "42 no es str" tal como se le indicó.