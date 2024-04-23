import csv

def escribirPlano(linea):
    with open("./datos.sen", "+w") as archivo:
        archivo.write(linea + "\n")
        
        
escribirPlano("Hola Mundo,")

def añadirPlano(linea):
    with open("./datos.sen", "a") as archivo:
        archivo.write(linea + "\n")
        
        
añadirPlano("Hello World,")

def LeerPLano():
    with open("./datos.sen", "r") as plano:
        leer = csv.reader(plano, delimiter= ",")
        for linea in leer:
            for nombre in linea:
                print(nombre)

# añadirPlano("ola, si, oa")
LeerPLano()