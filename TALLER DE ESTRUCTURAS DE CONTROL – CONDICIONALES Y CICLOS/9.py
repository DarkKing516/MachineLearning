total = 0
while True:
    monto = 0
    print("Cliente:")
    while True:
        precio = float(input("Ingrese el precio del artículo (o ingrese 0 para finalizar): "))
        
        if precio == 0:
            break
        
        monto += precio
    
    print(f"El monto a pagar del cliente es: ${monto}")
    
    total += monto
    
    continuar = input("¿Hay otro cliente? (Si/No): ").lower()
    if continuar != "si":
        break

print(f"El total cobrado al final del día es: ${total}")