"""
Se desea obtener el valor de la matricula de un estudiante cuyo valor se calcula de la siguiete manera

El valor de la matricula se calcula de la siguiente manera:
si es estudiante es mayor de 18 años el valor del credito es de 200.000
sino es de 150.000

si toma 30 o menos creditos paga normal
si toma más de 30 creditos pagará los creditos extras al doble del valor normal

si es de estrato 1, descuento del 80%
si es de estrato 2, descuento del 50%
si es de estrato 3, descuento del 30%
"""

edad = int(input("Digite su edad en años: "))

precioCredito = 0
if edad > 18:
    precioCredito = 200000
else:
    precioCredito = 150000

cantidadCreditos = int(input("Digite la cantidad de creditos: "))
totalCredito = 0
if cantidadCreditos <= 30:
    totalCredito = precioCredito * cantidadCreditos
    print(f"Usted pagará: ${totalCredito} como base por los creditos que pidió")

elif cantidadCreditos > 30:
    primerprecio = 30 * precioCredito
    precioCreditosDeMas = (cantidadCreditos - 30) * (precioCredito * 2)
    totalCredito = primerprecio + precioCreditosDeMas
    print(f"Usted pagará ${primerprecio} por los primeros 30 creditos y ${precioCreditosDeMas} por los {(cantidadCreditos - 30)} creditos que exceden los 30 creditos, un valor base de ${totalCredito}")


estrato = int(input("Digite su estrato: "))

if estrato == 1:
    descuento = 0.8
    valorConDescuento = totalCredito * descuento
    print(f"Tendrá un descuento de: ${valorConDescuento}")
    print(f"El valor total de su matricula es de: ${totalCredito - valorConDescuento}")

elif estrato == 2:
    descuento = 0.5
    valorConDescuento = totalCredito * descuento
    print(f"Tendrá un descuento de: ${valorConDescuento}")
    print(f"El valor total de su matricula es de: ${totalCredito - valorConDescuento}")


elif estrato == 3:
    descuento = 0.3
    valorConDescuento = totalCredito * descuento
    print(f"Tendrá un descuento de: ${valorConDescuento}")
    print(f"El valor total de su matricula es de: ${totalCredito - valorConDescuento}")
    
elif estrato != 1 and estrato != 2 and estrato != 3:
    print("El estrato ingresado no es válido")


