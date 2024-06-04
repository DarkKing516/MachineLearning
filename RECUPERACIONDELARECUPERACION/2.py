# Una empresa de envio de mercancias tiene un plan de tarifas y descuentos sobre el valor del envio de mercancia de sus clientes:

# Tarifas:
# Si el peso de la mercancia es inferior a 100kg,para el envio de esta es de 20000 pesos
# Si el peso de la mercancia esta entre 100 y 150kg, la tarifa para el envio de esta es de 25000
# si el peso de la mercancia es superior a 150kg  y menor o igual a 200kg, la tarifa para el envio de esta es de 30000 pesos
# si el peso de la mercancia es superior a 200kg, la tarifa es de 35000 y ademas por cada 10kg adicionales se paga 2000 pesos

# Descuentos
# si el valor de la mercancia esta entre 300000 y 600000 pesos se hace un descuento del 10% sobre el valor del envio
# si el valor de la mercancia es superior a 600000 pero menor o igual a 1000000 de pesos se hace un descuento del 20% sobre el valor del envio
# si el valor de la mercancia es superior a 1000000 se hace un descuento del 30% sobre el valor del envio

peso = int(input("Digite el peso de la mercancia: "))
mercancia = int(input("Digite el valor de la mercancia: "))
print("\n     Tarifas:     ")
if peso < 100:
    tarifa = 20000
    print(f"El valor de la tarifa es: ${tarifa}")

elif peso >= 100 and peso <= 150:
    tarifa = 25000
    print(f"El valor de la tarifa es: ${tarifa}")

elif peso > 150 and peso <= 200:
    tarifa = 30000
    print(f"El valor de la tarifa es: ${tarifa}")

elif peso > 200:
    tarifa = 35000
    print(f"El valor de la tarifa sin el peso adicional es: ${tarifa}")
    pesoAdicional = (peso - 200) * 2000
    print(f"El valor de los pesos adicionales es: ${pesoAdicional}")
    tarifa += pesoAdicional
    print(f"El valor de la tarifa es: ${tarifa}")

print("\n     Descuentos:     ")
if mercancia >= 300000 and mercancia <= 600000:
    descuento = tarifa * 0.10
    print(f"El valor del descuento es: ${descuento}")
    tarifa -= descuento
    print(f"El valor de la tarifa total es: ${tarifa}")

elif mercancia > 600000 and mercancia <= 1000000:
    descuento = tarifa * 0.20
    print(f"El valor del descuento es: ${descuento}")
    tarifa -= descuento
    print(f"El valor de la tarifa total es: ${tarifa}")

elif mercancia > 1000000:
    descuento = tarifa * 0.3
    print(f"El valor del descuento es: ${descuento}")
    tarifa -= descuento
    print(f"El valor de la tarifa total es: ${tarifa}")
elif mercancia < 300000:
    print(f"El valor de la tarifa total es: ${tarifa}")
    print("No hay descuento.")