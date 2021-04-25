### FICHEROS
# PREGUNTA 1

def tabla_n():
    while True:
        try:
            n = int(input("Introduce un número entero del 1 al 10: "))
            if n >= 1 and n <= 10:
                break
            else:
                print("Intente nuevamente, el número debe estar entre 1 y 10")
        except:
            print("Introduce un número válido")
    
    with open(f'./tabla-{n}.txt',mode='w') as f:
        for i in range(0, 11):
            f.write(f"{n} x {i} = {n*i}\n")
        print(f"El archivo tabla-{n}.txt se creó en la ruta actual de forma satisfactoria")
        f.close
    
tabla_n()

print ("")


# PREGUNTA 2

def ver_tabla():
    while True:
        try:
            n = int(input("Introduce un número entero del 1 al 10:"))
            if n >= 1 and n <= 10:
                break
            else:
                print("Intente nuevamente, el número debe estar entre 1 y 10")
        except:
            print("Introduce un número válido")
    try:
        with open(f'./tabla-{n}.txt',mode='r') as f:
            texto = f.readlines()
            for fila in texto:
                print(fila)
    except:
        print("¡ERROR¡ No existe la tabla almacenada para ese número")

ver_tabla()

print ("")


# PREGUNTA 3

def buscar_tabla():
    while True:
        try:
            n = int(input("Introduce el primer número entero del 1 al 10:"))
            if n >= 1 and n <= 10:
                while True:
                    try:
                        m = int(input("Introduce el segundo número entero del 1 al 10:"))
                        if m >= 1 and m <= 10:
                            break
                        else:
                            print("Intente nuevamente, el número debe estar entre 1 y 10")
                    except:
                        print("Introduce un número válido")
                break
            else:
                print("El número debe estar entre 1 y 10")
        except:
            print("Introduce un número válido")
    
    try:
        with open(f'./tabla-{n}.txt',mode='r') as f:
            texto = f.readlines()
            for fila in texto:
                if fila == f"{n} x {m} = {n*m}\n":
                    print(fila)
    except:
        print("Ese producto no está almacenado en ningún archivo de tabla")

buscar_tabla()
