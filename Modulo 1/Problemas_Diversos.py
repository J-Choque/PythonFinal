# PROBLEMA 1

m = float(input('Ingrese cantidad de dinero depositada en la cuenta de ahorros: '))

i = 0.04

for a in range (1,4):
    m = m * (1+i)
    print (f"El monto al final del año {a} es :{round(m,2)}")

print ("")



# PROBLEMA 2

from math import sqrt

a = int(input ('Ingrese un valor diferente a 0: '))
b = int(input ('Ingrese un valor de b: '))
c = int(input ('Ingrese un valor de c: '))

if a!=0:
    #Calculo de la discriminante
    d = (b**2 - 4*a*c)
    
    if d < 0:
        print ('Ecuacion no presenta solución real')
    else:
        x1 = (-b + sqrt(d))/(2*a)
        x2 = (-b - sqrt(d))/(2*a)
        print (f'Los valores son {x1} y {x2}')

else:
    print ('El valor de a debe ser distinto a cero')
     
