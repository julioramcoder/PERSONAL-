def crear_archivotxt (nombre):
    with open (nombre, "w") as file:
        file.write("mi primer archivo creado en python")
        return f" el archivo {nombre} fue creado correctamente"
    
#ahora vamos a crear una funcion para agregar 

def agregar_notas (nombre, text):
    with open (nombre, text) as file: 
        file.write(text)
        return("texto agregado")
    
def leer_archivo (nombre):
    with open (nombre, "r") as file:
        file.read("archivo leido")
        
        
        

    