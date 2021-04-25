# PROBLEMA 1

lista_alumnos = []

def alumnos(lista_alumnos, cantidad):
    for _ in range(cantidad):
        n = 0
        alumno = {}
        nombre = input(f"Ingrese el nombre completo del Alumno {len(lista_alumnos) + 1}: ")
        
        alumno['Nombre'] = nombre
        
        while n < 3:
            try:
                nota = float(input(f"Ingresa la nota {n + 1}: "))
                if nota >= 0 and nota <= 10:
                    alumno[f'Nota {n+1}'] = nota
                    n = n+1
                else:
                    print("¡ERROR¡ La nota debe estar comprendida entre 0 y 10")
            except:
                print("Ingrese una nota valida.")
        lista_alumnos.append(alumno)

while True:
    try:
        cantidad = int(input("Cantidad de alumnos: "))
        if cantidad <= 0:
            print("¡ERROR¡ Se debe ingresar una cantidad de alumnos mayor a 0")
        else:
            break
    except:
        print("¡ERROR¡ Por favor ingrese un valor de cantidad válido: ")

alumnos(lista_alumnos, cantidad)

lista_alumnos

print("")


# PROBLEMA 2

def promedio (lista_alumnos):
    for alumno in lista_alumnos:
        promedio = (alumno['Nota 1'] + alumno['Nota 2'] + alumno['Nota 3']) / 3
        alumno['promedio'] = promedio

def evaluar(lista_alumnos):
    aprobados = 0
    desaprobados = 0
    
    promedio(lista_alumnos)

    for alumno in lista_alumnos:
        if alumno['promedio'] >= 4:
            alumno['estado'] = 'Aprobado'
            aprobados += 1
        else:
            alumno['estado'] = 'Desaprobado'
            desaprobados += 1

    print(f'La cantidad de alumnos aprobados es de: {aprobados}')
    print(f'La cantidad de alumnos desaprobados es de: {desaprobados}')

evaluar(lista_alumnos)

print("")


# PROBLEMA 3

def promedio_curso(lista_alumnos):
    promedio = 0

    for alumno in lista_alumnos:
        promedio += alumno['promedio']

    return promedio / len(lista_alumnos)

print(f"El promedio de nota del curso total es: {promedio_curso(lista_alumnos)}")

print("")


# PROBLEMA 4

def puesto_promedio(lista_alumnos):
    palto = 0
    pbajo = 10
    
    for alumno in lista_alumnos:
        _ = alumno['Nombre']
        if alumno['promedio'] >= palto:
            alumno_alto = alumno['Nombre']
            palto = alumno['promedio']
        if alumno['promedio'] <= pbajo:
            alumno_bajo = alumno['Nombre']
            pbajo = alumno['promedio']
    
    print(f"El alumno con el promedio más alto es: {alumno_alto}")
    
    print(f"El alumno con el promedio más bajo es: {alumno_bajo}")

puesto_promedio(lista_alumnos)

print("")


# PROBLEMA 5

def buscar_alumno(nombre, lista_alumnos):
    for alumno in lista_alumnos:
        if alumno['Nombre'] == nombre:
            print(alumno)
            
nombre = input("Ingrese el nombre del o los alumnos a buscar: ")

buscar_alumno(nombre, lista_alumnos)