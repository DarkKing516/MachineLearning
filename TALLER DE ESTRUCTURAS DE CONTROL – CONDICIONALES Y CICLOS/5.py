
tamanio_bosque_hectareas = float(input("Ingrese el tamaño del bosque en hectáreas: "))


tamanio_bosque_metros_cuadrados = tamanio_bosque_hectareas * 10000


if tamanio_bosque_metros_cuadrados > 1000000:  
    porcentaje_pino = 0.70
    porcentaje_oyamel = 0.20
    porcentaje_cedro = 0.10
else:
    porcentaje_pino = 0.50
    porcentaje_oyamel = 0.30
    porcentaje_cedro = 0.20


cantidad_pinos = (porcentaje_pino * tamanio_bosque_metros_cuadrados) / 10
cantidad_oyameles = (porcentaje_oyamel * tamanio_bosque_metros_cuadrados) / 15
cantidad_cedros = (porcentaje_cedro * tamanio_bosque_metros_cuadrados) / 18


print(f"Número de pinos a sembrar: {int(cantidad_pinos)}")
print(f"Número de oyameles a sembrar: {int(cantidad_oyameles)}")
print(f"Número de cedros a sembrar: {int(cantidad_cedros)}")
