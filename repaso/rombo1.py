conter = 0
limite = int(input("Digité un numero: "))
espacios = ""

resta =  limite
print(f"{(' ' * limite)}#")
while conter < limite:
    conter = conter + 1
    # print(conter)
    resta -= 1
    print(f"{(' ' * resta)}#{" " * conter}{espacios}#")
    espacios = espacios + " "

    
band = True
suma = 0
resta2 = limite
while band:
    if conter == 0:
        band = False
    conter = conter - 1
    if conter < 1:
        break
    # print(conter)
    suma += 1
    resta2 -= 1
    espacios = espacios + " "
    print(f"{(' ' * suma)}#{" " * conter}{resta2 * ' '}#")
print(f"{(' ' * limite)}#")