from funcion_ingresar import *

def Sumar(num1, num2):
    print(f"La suma de los números es: {num1 + num2}")

def Restar(num1, num2):
    print(f"El resto de los números es: {num1 - num2}")
    
def Multiplicar(num1, num2):
    print(f"El producto de los números es: {num1 * num2}")

def Dividir(num1, num2):
    print(f"El cociente de los números es: {num1 / num2}")

opcion = 1

while(opcion != 0):
    print("Este es un menú de funciones")
    print("1. Ingresar los números")
    print("2. Sumar números")
    print("3. Restar números")
    print("4. Multipliar números")
    print("5. Dividir números")
    print("0. Salir")

    opcion = int(input("Ingrese una opción: "))
    
    if(opcion == 1):
        num1, num2 = Ingresar()
    elif(opcion == 2):
        Sumar(num1, num2)
        print("\n================================")
    elif(opcion == 3):
        Restar(num1, num2)
        print("\n================================")
    elif(opcion == 4):
        Multiplicar(num1, num2)
        print("\n================================")
    elif(opcion == 5):
        Dividir(num1, num2)
        print("\n================================")
    elif(opcion == 0):
        print("Saliendo...")
        break
    else:
        print("Opción no valida")
        
