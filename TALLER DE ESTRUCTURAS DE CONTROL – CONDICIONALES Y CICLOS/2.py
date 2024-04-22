print("""
Resultados obtenidos en un laboratorio de análisis clínicos:

EDAD NIVEL HEMOGLOBINA
0 - 1 mes            13 - 26 g%
> 1 y < = 6 meses    10 - 18 g%
> 6 y < = 12 meses   11 - 15 g%
> 1 y < = 5 años     11.5 - 15 g%
> 5 y < = 10 años    12.6 - 15.5 g%
> 10 y < = 15 años   13 - 15.5 g%
mujeres > 15 años    12 - 16 g%
hombres > 15 años    14 - 18 g%
""")
edad = float(input("Ingrese la edad en años: "))
sexo = input("Ingrese el sexo (Mujer/Hombre): ").lower()
nivel_hemoglobina = float(input("Ingrese el nivel de hemoglobina en g%: "))

anemia = False
if edad <= 1/12:
    if nivel_hemoglobina < 13:
        anemia = True
elif 1/12 < edad <= 6/12:
    if nivel_hemoglobina < 10:
        anemia = True
elif 6/12 < edad <= 12/12:
    if nivel_hemoglobina < 11:
        anemia = True
elif 1 < edad <= 5:
    if nivel_hemoglobina < 11.5:
        anemia = True
elif 5 < edad <= 10:
    if nivel_hemoglobina < 12.6:
        anemia = True
elif 10 < edad <= 15:
    if nivel_hemoglobina < 13:
        anemia = True
elif sexo == "mujer" and edad > 15:
    if nivel_hemoglobina < 12:
        anemia = True
elif sexo == "hombre" and edad > 15:
    if nivel_hemoglobina < 14:
        anemia = True

if anemia:
    print("La persona tiene anemia.")
else:
    print("La persona no tiene anemia.")