"""
300000 por primeros 400 km
más de 400km hasta 1000km cobra 18000 adicional por cada kilometro sobre los 400
más de 1000km cobra un monto adicional de 10000 por cada kilometro sobre los 1000
los precios ya incluyen el 20% de impuesto general a las ventas IVA

los precios ya incluyen el 20% del impuesto general a las ventas IVA. Diseñe un algoritmo que determine el monto a pagar por el alquiler de un vehiculo y el monto incluido del impuesto
"""
montofijo = 300000

kilometros = int(input("Digité los kilometros recorridos por el vehiculo: "))

if kilometros < 400:
    print(f"Para los primeros 400 kilometros debe pagar un monto fijo de: ${montofijo}")
elif kilometros > 400 and kilometros < 1000:
    montoAdicional = (kilometros - 400) * 18000
    montofijo += montoAdicional
    print(f"Debe pagar un monto total de ${montofijo} ya que sobrepasó los primeros 400 kilometros, recorrió un total de {kilometros - 400} kilometros encima de los 400; pagó un adicional de : ${montoAdicional}")
elif kilometros > 1000:
    montoAdicional = (kilometros - 1000) * 10000
    montofijo += montoAdicional
    print(f"Debe pagar un monto total de ${montofijo} ya que sobrepasó los primeros 1000 kilometros, recorrió un total de {kilometros - 1000} kilometros encima de los 1000; pagó un adicional de : ${montoAdicional}")