#Definiendo clase
class Tarjeta:
    def __init__(self, numtarjeta):
        self.numtarjeta = numtarjeta

    # Función booleana que realiza el Algoritmo Luhn para verificar si la tarjeta cumple o no con este
    def Luhn(self):
            pos1 = len(self.numtarjeta) - 2
            pos2 = len(self.numtarjeta) - 1
            suma1 = 0
            suma2 = 0
    
            while (pos1 + pos2) >= -1:
                i = int(self.numtarjeta[pos1])
                j = int(self.numtarjeta[pos2])

                if pos1 != -1:    
                    if i*2 >= 10:
                        suma1 = suma1 + int(i*2/10) + (i*2)%10
                    else:
                        suma1 = suma1 + i*2
                
                suma2 = suma2 + j
    
                pos1 = pos1 - 2
                pos2 = pos2 - 2
            
            if (suma1 + suma2)%10 == 0:
                return True
            else:
                return False
    
    # Se valida la tarjeta según la longitud de la misma y si cumple con el algoritmo Luhn
    def validar(self):
        if (len(self.numtarjeta) == 15 or len(self.numtarjeta) == 16 or len(self.numtarjeta) == 13) and self.Luhn():
            return True
        else:
            return False

    # Usando las función de validación y de acuerdo a las características de algunos dígitos de la tarjeta, se categoriza su tipo
    def tipo(self):
        if self.validar():
            if len(self.numtarjeta) == 15 and (self.numtarjeta[0:2] == '34' or self.numtarjeta[0:2] == '37'):
                print("AMEX\n")
            elif len(self.numtarjeta) == 16  and (self.numtarjeta[0:2] == '51' or self.numtarjeta[0:2] == '52' or self.numtarjeta[0:2] == '53' or self.numtarjeta[0:2] == '54' or self.numtarjeta[0:2] == '55'):
                print("MASTERCARD\n")
            elif (len(self.numtarjeta) == 13 or len(self.numtarjeta) == 16) and self.numtarjeta[0] == '4':
                print("VISA\n")
            else:
                print("INVALID\n")
        else:
            print("INVALID\n")

#Programa principal
if __name__ == '__main__':
    #Se define la función pedir tarjeta
    def pedirtarjeta():
        while True:
            numtarjeta = input("Introduce tu número de tarjeta: ")
            for digito in numtarjeta:
                #Para validar que todos los digitos de la tarjeta sean números, se hace la siguiente validación
                try:
                    _ = int(digito)
                    valido = True
                except:
                    valido = False
                    print("El número de tarjeta solo puede contener números")
                    break
            #Si la tarjeta solo contiene números, se hace un break en el while
            if valido:
                break

        #Se crea un objeto de la clase Tarjeta con el parámetro numtarjeta
        tarjeta = Tarjeta(numtarjeta)
    
        #Se utiliza el método tipo para imprimir los resultados requeridos
        tarjeta.tipo()

pedirtarjeta()