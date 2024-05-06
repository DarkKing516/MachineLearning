"""
Contar el número de letras que existe en un parrafo y decir cual es la que más se repite
"""
parrafo = input("Digite el parrafo para contar sus letras (no contaremos los espacios en el parrafo ni comas ni puntos): ")
parrafo = parrafo.lower().replace('.', '').replace(',', '').replace(' ', '')

letras = {}
for letra in parrafo:
    if letra.isalpha():
        if letra in letras:
            letras[letra] += 1
        else:
            letras[letra] = 1

letraReptida = max(letras, key=letras.get)
print(f"El parrafo tiene {len(parrafo)} letras")
print(f"La letra más repetida es '{letraReptida}' con {letras[letraReptida]} ocurrencias")