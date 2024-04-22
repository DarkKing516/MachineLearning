descuento = 0

print("""
        Tabla de descuentos:
NUM. DE KILOS COMPRADOS   % DESCUENTO
--------------------------------------
0 - 2                  0%
2.01 - 5               10%
5.01 - 10              15%
10.01 en adelante      20%
""")

cantidad = float(input("Digite la cantidad de kilos que compró de manzanas: "))

precio = float(input("Digite la cantidad a pagar por las manzanas: "))

if cantidad <= 2:
    descuento = 0
elif cantidad <= 5:
    descuento = 0.10
elif cantidad <= 10:
    descuento = 0.15
else:
    descuento = 0.20

total = (precio * descuento) + precio

print(f"El descuento será de: {int(descuento * 100)}%")

print(f"El total será de: {format(total)}")
