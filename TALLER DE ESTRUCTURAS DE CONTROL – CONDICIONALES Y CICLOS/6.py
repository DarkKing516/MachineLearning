numeros= []
datos = int(input("Ingrese el número de datos: "))
for i in range(1, (datos + 1)):
    nuevoNum = int(input(f"Digite el {i}° número: "))
    numeros.append(nuevoNum)

numeros.sort()

valor_minimo = numeros[0]
frecuencia_minimo = numeros.count(valor_minimo)

print(f"El valor mínimo es: {valor_minimo}")
print(f"Se presenta {frecuencia_minimo}, veces en el grupo de datos.")
