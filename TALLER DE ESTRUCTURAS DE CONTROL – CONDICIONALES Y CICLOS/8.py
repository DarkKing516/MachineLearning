total = 0
while True:
    precio = float(input("Ingrese el precio del artículo (o ingrese 0 para finalizar): "))
    
    if precio == 0:
        break
    
    cantidad = int(input("Ingrese la cantidad de artículos: "))
    
    costo = precio * cantidad
    total += costo
print(f"El total de la compra es: ${total}")
