# Pasajes de parámetros por valor y referencia y Funciones Lambda

# El comportamiento de paso de parámetros por valor o ref depende del tipo de dato:
# Si usamos un parámetro pasado por valor, se creará una copia local de la variable, lo que implica
# que cualquier modificación sobre la misma no tendrá efecto sobre la original.

x = 10
def funcion(entrada):
    entrada=0

funcion(x)
print(x) # Vemos que x no ha sido modificada
print("--------------------------------------------")

# Con una variable pasada como referencia, se actuará directamente sobre la variable pasada, 
# por lo que las modificaciones afectarán a la variable original.
# Ej:

x = [10, 20, 30]
def funcion(entrada):
    entrada.append(40)
funcion(x)
print(x) # Vemos que la variables original x ha sido modificada

# En Python los tipos de datos simples se pasan como valor (int, float, string, bool, complex),
# los demás tipos de datos, se pasan como referencia.

# Copy() Este método únicamente se encarga de copiar el objeto que hemos pasado como argumento,
# independientemente si contiene en su interior otros objetos mutables. 

x=[1,2]
y=x.copy() # Evitamos que el ID de x sea el mismo que el de y
y.append(3) # A la hora de lamar a x mantendrá su valor original, no sufrirá cambios
print(id(x))
print(id(y))

# Funciones Lambda
# Las funciones Lambda son una forma conveniente de crear una función en una sola línea en Python. También se las conoce como funciones anónimas, ya que no tienen nombre y se asignan a una variable.

# A diferencia de las funciones regulares, las funciones Lambda pueden tener cualquier cantidad de argumentos, pero solo una expresión. Además, no necesitan un return, ya que la expresión es el valor de retorno.

lambda_producto = lambda x, y: x * y

lambda_producto(3, 4)

