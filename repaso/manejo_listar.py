import random
lista = []
def Ingresar():
    rango = int(input("Ingrese el número de datos que tendrá la lista: "))
    for i in range(rango):
        nuevoNum = int(input(f"Digite el {i + 1}° número: "))
        lista.append(nuevoNum)
    return lista

def BuscarDato(dato):
    if dato in lista:
        print(f"El dato {dato} se encuentra en la lista")
    else:
        print(f"El dato {dato} no se encuentra en la lista")


print("Manejo de Listas")

opcion = 1
while opcion != 0:
    print("Menú")
    opcion = int(input("""
    1. Ingresar datos de la lista
    2. Mostrar datos de la lista
    3. Buscar dato de la lista
    4. Ordenar datos de la lista
    5. Remover dato de la lista
    0.Salir
    """))
    
    if opcion != 1 and lista == []:
        print("Primero debe ingresar datos a la lista.\n")
        continue
    
    match opcion:
        case 1:
            Ingresar()
            print("\n================================================")
        case 2:
            print(lista)
            print("\n================================================")
        case 3:
            dato = int(input("Ingrese el dato a buscar: "))
            BuscarDato(dato)
            print("\n================================================")
        case _:
            print("Opción no valida")