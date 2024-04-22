numeros = []

for i in range(1, 4):
    nuevoNum = int(input(f"Digite el {i}° número: "))
    numeros.append(nuevoNum)

numeros.sort()
# if numeros[0] < numeros[1] < numeros[2] or numeros[2] < numeros[1] < numeros[0]:
#     medio = numeros[1]
# elif numeros[1] < numeros[0] < numeros[2] or numeros[2] < numeros[0] < numeros[1]:
#     medio = numeros[0]
# else:
#     medio = numeros[2]
medio = numeros[1]

print(f"El número medio es: {medio}")
