import csv

def escribirPlano(linea):
    with open("./datos.sen", "+w") as archivo:
        archivo.write(linea + "\n")
        
        
escribirPlano("Hola Mundo")