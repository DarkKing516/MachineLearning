import random
lista = []

# for i in range(10):
#     lista.append(int(input(f"Digite el {i}° número: ")))

for i in range(10):
    lista.append(random.randint(0, 50))

print(lista)
print(lista[1:4])

tupla = (lista)
tupla.append(1)
# tupla.sort()
tupla[-1]= 9
print(tupla)

sete = {23, 4, 5, 7, 10}
sete1 = {0, 13, 15, 10, 24}
print(sete - sete1)
print(sete & sete1)
print(sete | sete1)

diccionario1 = {
    "carro": "raio makuin",
    "modelo": 2008,
    "empresa": "BBVA"
}

print(diccionario1)
print(diccionario1["empresa"])

for clave, valor in diccionario1.items():
    print(f"{clave} = {valor}")

for clave in diccionario1.keys():
    print(f"{clave} = {diccionario1[clave]}")
    
