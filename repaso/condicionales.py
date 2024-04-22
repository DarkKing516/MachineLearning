num1 = int(input("Digite un número: "))
num2 = int(input("Digite otro número: "))

if num1 == num2:
    print("Los números son iguales")
    print(f"La suma de los números es: {num1 + num2}")
    
elif num1 > num2:
    print(f"El número {num1} es mayor que {num2}")
    print(f"La suma de los números es: {num1 + num2}")
    
elif num2 > num1:
    print(f"El número {num2} es mayor que {num1}")
    print(f"La suma de los números es: {num1 + num2}")
    
else:
    print("Error: Los números no son válidos")
