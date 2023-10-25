# Polimorfismo

# Proviene de poli = muchas, morfismo = formas. Se utiliza para crear métodos con el mismo nombre
# pero con diferente comportamiento.

# Abstracción

# El encapsulamiento es como un cofre con una cerradura. Los datos y comportamientos de una clase
# se almacenan dentro del "cofre" y solo se pueden acceder a ellos a través de métodos públicos
# autorizados, como si tuvieras la "llave" para abrir el cofre. Esto ayuda a prevenir la modificación
# accidental o no autorizada de los datos y comportamientos de la clase.

# Encapsulamiento

# Se utiliza cuando es necesario que ciertos métodos o propiedades sean inviolables o inalterables.
# Se refiere a la ocultación de los detalles internos de una clase para proteger los datos y 
# comportamientos de esa clase de accesos no autorizados o modificaciones accidentales.

# El encapsulamiento es como un cofre con una cerradura. Los datos y comportamientos de una clase
# se almacenan dentro del "cofre" y solo se pueden acceder a ellos a través de métodos públicos
# autorizados, como si tuvieras la "llave" para abrir el cofre. Esto ayuda a prevenir la modificación
# accidental o no autorizada de los datos y comportamientos de la clase.

# Ej:
class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # el atributo saldo está encapsulado con __

    def depositar(self, monto):
        self.__saldo += monto

    def retirar(self, monto):
        if self.__saldo >= monto:
            self.__saldo -= monto
        else:
            print("Saldo insuficiente")

    def obtener_saldo(self):
        return self.__saldo

# Herencia

# Permite crear nuevas clases a partir de otras. Al tener la clase Gato, pudimos crear el objeto 
# gato1, con los atributos que ya vimos, podemos crear gato2, que va también a tomar propiedades 
# y métodos de la clase Gato. Esto nos da una jerarquía de padre e hijo.

# La herencia en Python es especialmente útil para crear clases especializadas, también conocidas
# como clases derivadas o subclases. Al heredar de una clase base, puedes extender su funcionalidad
# y personalizarla según tus necesidades específicas.

# Al heredar de una clase base, la clase hija puede acceder a todos los atributos y métodos de la clase
# base. Esto te permite utilizar y modificar los atributos y métodos heredados, así como agregar nuevos
# atributos y métodos propios que son relevantes para la especialización.

# Ej:

class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    # Método genérico pero con implementación particular
    def hablar(self):
        # Método vacío
        pass

    # Método genérico pero con implementación particular
    def moverse(self):
        # Método vacío
        pass

    # Método genérico con la misma implementación
    def describeme(self):
        print("Soy un Animal del tipo", type(self).__name__)

class Perro(Animal):
    def hablar(self):
        print("Guau!")
    def moverse(self):
        print("Caminando con 4 patas")

class Vaca(Animal):
    def hablar(self):
        print("Muuu!")
    def moverse(self):
        print("Caminando con 4 patas")

class Abeja(Animal):
    def hablar(self):
        print("Bzzzz!")
    def moverse(self):
        print("Volando")

    # Nuevo método
    def picar(self):
        print("Picar!")


# Al llamar a super(), se obtiene una referencia al objeto de la clase padre, lo que permite invocar
# los métodos de la clase base y aprovechar su implementación existente. La sintaxis para usar super()
# es simple: super().metodo() llama al método deseado de la clase padre.

# Ej opción sin super():

class Serpiente(Animal):
    def __init__(self,especie,edad,dueño):
        self.especie = especie
        self.edad = edad
        self.dueño = dueño
    
# Ej opción con super():

class Serpiente(Animal):
    def __init__(self,especie,edad,dueño):
        super().__init__(especie,edad)
        # Con super llamamos al __init de la clase padre y NO requerimos usar self, y debajo agregamos el nuevo
        self.dueño = dueño   
