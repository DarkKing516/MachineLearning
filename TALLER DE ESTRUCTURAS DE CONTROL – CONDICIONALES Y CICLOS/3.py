promedio = float(input("Ingrese el promedio del alumno: "))
alumno = input("Ingrese el nivel del alumno (Preparatoria/Profesional): ")
reprobadas = int(input("Ingrese el número de materias reprobadas del alumno: "))
unidades = 0
costoUnidad = 0
descuento = 0
if alumno == "Preparatoria":
    costoUnidad = 180
    if promedio >= 9.5:
        unidades = 55
        descuento = 0.25
    elif 9 <= promedio < 9.5:
        unidades = 50
        descuento = 0.10
    elif 7 < promedio < 9:
        unidades = 50
        descuento = 0
    elif promedio <= 7 and 0 <= reprobadas <= 3:
        unidades = 45
        descuento = 0
    elif promedio <= 7 and reprobadas >= 4:
        unidades = 40
        descuento = 0
elif alumno == "Profesional":
    costoUnidad = 300
    if promedio >= 9.5:
        unidades = 55
        descuento = 0.20
    else:
        unidades = 55
        descuento = 0

subtotal = (unidades * costoUnidad) * descuento
total = (unidades * costoUnidad) - subtotal

print(f"El total a pagar del alumno es: ${total}")
