limite = int(input("Ingrese un número impar para el tamaño del rombo: "))

while limite % 2 == 0:
    limite = int(input("Por favor, ingrese un número impar: "))

for i in range(1, limite + 1, 2):
    espacios = (limite - i) // 2
    print(" " * espacios + "#" + " " * (i - 2) + ("#" if i > 1 else ""))

for i in range(limite - 2, 0, -2):
    espacios = (limite - i) // 2
    print(" " * espacios + "#" + " " * (i - 2) + ("#" if i > 1 else ""))
