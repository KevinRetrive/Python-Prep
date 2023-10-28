class Funciones_2():
    def __init__(self,lista_final):
        if type(lista_final)!=list:
            self.lista_final=[]
            raise ValueError("Se ingresaron tipo de datos inválidos, se esperaba una lista de números enteros")
        else:
            self.lista_final=lista_final

    def facto(self):
        for i in self.lista_final:
            print('El factorial de ', i, 'es', self._facto(i))
            
    def convertidor_temp(self, origen, destino):
        parametros_esperados=["Celsius","Farenheit","Kelvin"]
        lista_conversion=[]
        if str(origen) not in parametros_esperados:
            print(f"Los parámetros permitidos son: {parametros_esperados}")
        if str(destino) not in parametros_esperados:
            print(f"Los parámetros permitidos son: {parametros_esperados}")
        for i in self.lista_final:
            lista_conversion.append(self._convertidor_temp(i,origen,destino))
        return lista_conversion

    def es_primo(self):
        for i in self.lista_final:
            if (self._es_primo(i)):
                print('Elemento', i, 'SI primo')
            else:
                print('Elemento', i, 'NO primo')
        
    def _facto(self,num): # Agregar self a todos
        if (num <0 or type(num)==float):
            return "Error. Se debe ingresar un n° entero y positivo"
        if num>1: 
            num=num*self._facto(num-1)
            return num
        if num == 0:
            num=1
        return num
        
    def _convertidor_temp(self,temperatura,origen,destino):
        if (origen == "Celsius" and destino == "Kelvin"):
            temperatura_new=temperatura+273.15
        elif (origen == "Celsius" and destino == "Farenheit"):
            temperatura_new=temperatura*9/5+32
        elif (origen == "Kelvin" and destino == "Celsius"):
            temperatura_new=temperatura-273.15
        elif (origen == "Kelvin" and destino == "Farenheit"):
            temperatura_new=temperatura*9/5-459.67
        elif (origen == "Farenheit" and destino == "Kelvin"):
            temperatura_new=(temperatura+459.67)*5/9
        elif (origen == "Farenheit" and destino == "Celsius"):
            temperatura_new=(temperatura-32)*5/9
        elif origen == destino:
            temperatura_new=temperatura
            print(f"La unidad de origen es igual a la de destino:")
        return round(temperatura_new,2)
    
    def repetidos(self):
        lista_sinrepe = []
        lista_repe = []
        if len(self.lista_final==0):
            return None
        #if (menor):
        #    self.lista_final.sort()
        for elem in self.lista_final:
            if  elem in lista_sinrepe:
                i=lista_sinrepe.index(elem)
                lista_repe[i]+=1
            else:
                lista_sinrepe.append(elem)
                lista_repe.append(1) #Inicio el contador de repeticiones para ese elemento en 1
        val = lista_sinrepe[0]  # Se asume que el primer elemento de la lista de únicos es la moda inicialmente
        max = lista_repe[0]  # Se asume que el primer contador de repeticiones es el máximo inicialmente
        for i, elemento in enumerate(lista_sinrepe):  # Iteración sobre cada elemento único y su índice
            if lista_repe[i] > max:  # Verificación si el contador de repeticiones es mayor al máximo actual
                val = lista_sinrepe[i]  # Se actualiza la moda con el nuevo elemento con más repeticiones
                max = lista_repe[i]  # Se actualiza el máximo con el nuevo contador de repeticiones mayor
        return val, max  # Se devuelve la moda y el máximo de repeticiones como una tupla
    
    def _es_primo(self,num):
        prim = True
        for i in range(2,num):
            if num%i==0: # O sea, que divido el nro por todos los n° anteriores para chequear que sea primo
                prim=False
                break
        return prim
    
    def extrae_primos(self,lista_num):
        lista_primos=[]
        for elem in lista_num:
            if self.es_primo(int(elem)):
                lista_primos.append(elem)
        return f"El conjunto de n° primos es: {lista_primos}"
    
F2=Funciones_2([1,1,2,5,8,8,9,11,15,16,16,16,18,20])
    
#Primos=F2.es_primo
#print(Primos) # No entiendo por que era que no me da el resultado acá..