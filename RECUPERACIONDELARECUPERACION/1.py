# Realizar un algoritmo que me permita ingresar un número determinado de segundos y lo convierta en horas, minutos y segundos

# 3600 segundos una hora
# 3601 segundos una hora y un segundo

segundos = int(input("Digite los segundos: "))

horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos = (segundos % 3600) % 60

print(f"{horas} horas, {minutos} minutos y {segundos} segundos")
