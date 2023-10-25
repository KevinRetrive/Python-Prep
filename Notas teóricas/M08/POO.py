# La programación orientada a objetos (POO) en Python es un paradigma de programación que se basa
# en el concepto de objetos y clases. En lugar de enfocarse únicamente en las acciones y funciones
# que se deben realizar, la POO se centra en la creación de objetos, que son instancias de clases.
# Una clase es una plantilla que define las características y el comportamiento de un objeto.

# Clases

# Declaración de clase: Para definir una clase, utilizamos la palabra clave class seguida del nombre
# de la clase. Por ejemplo, podríamos tener una clase llamada "Perro".

# Atributos de clase: Los atributos de clase son variables que pertenecen a la clase en su conjunto.
# Se definen dentro de la clase, pero fuera de cualquier método. Pueden ser accedidos por todas las
# instancias de la clase. Por ejemplo, un atributo de clase podría ser "especie" con el valor "canino".

# Método __init__: Es un método especial en Python que se llama automáticamente cuando se crea un nuevo
# objeto de una clase. Se utiliza para inicializar los atributos de instancia del objeto. 
# Se define dentro de la clase y tiene el nombre __init__.

# Atributos de instancia: Los atributos de instancia son variables específicas de cada objeto creado
# a partir de la clase. Se definen dentro del método __init__ utilizando el parámetro self. 
# Por ejemplo, en la clase "Perro", podríamos tener atributos de instancia como "nombre" y "edad".

# Métodos: Los métodos son funciones definidas dentro de la clase y se utilizan para realizar acciones
# o manipular los atributos de instancia de los objetos. Estos métodos también se definen utilizando 
# el parámetro self para acceder a los atributos y otros métodos de la clase.

# Creación de objetos: Una vez que hemos definido nuestra clase, podemos crear objetos a partir de ella.
# Para crear un objeto, simplemente llamamos al nombre de la clase como si fuera una función. 
# Por ejemplo, podemos crear un objeto "mi_perro" utilizando la clase "Perro".

#Ej:

class Gato:
    def __init__(self, nombre, edad,raza, sexo): # __init__ constructor de la clase
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.sexo = sexo
   #Creamos el método presentar
    def presentar(self):
        print("Mi Nombre: ", self.nombre)
        print("Edad: ", self.edad,"años")
        print("Raza: ", self.raza)
        print("Sexo: ", self.sexo)

michi=Gato("Puerquita","desconocida","gordita","no binaria")
michi.presentar()