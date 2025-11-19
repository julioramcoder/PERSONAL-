import json

def guardar_json (nombre, data):
    with open (nombre, "w") as f:
        json.dump(data,f, indent=4) #json es una funcion netamente de python #indet=4 nos ayuda a que 