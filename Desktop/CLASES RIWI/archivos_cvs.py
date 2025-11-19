import csv

def crear_csv(nombre,encabezado):
    with open (nombre, "w", newline="") as f:#newline==""  que aparte de la informacion que yo le de al encabezado no me permita nada mas:
        write = csv.writer(f)
        write.writerow (encabezado)#writeow es escribir una sola linea
        
def usuariotipo_csv(nombre,encabezado):
    with open (nombre, "w", newline="") as f:#newline==""  que aparte de la informacion que yo le de al encabezado no me permita nada mas:
        write = csv.writer(f)
        write.writerow (encabezado)#writeow es escribir una sola linea

def agregar_linea (nombre, datos):
    with open(nombre, "a", newline="") as file:
        writer=csv.writer(file)
        writer.writerow(datos)

def usuariotipo_csv(nombre,datos):
    with open (nombre, "a", newline="") as f:#newline==""  que aparte de la informacion que yo le de al encabezado no me permita nada mas:
        write = csv.writer(f)
        write.writerow (datos)#writeow es escribir una sola linea
