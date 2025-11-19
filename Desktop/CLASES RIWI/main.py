
from archivos_cvs import usuariotipo_csv, agregar_linea, usuariotipo_csv
print(usuariotipo_csv("usuariotipo.csv",["usuario","id"]))
print(agregar_linea("coders.csv",["andres","26"]))
print(usuariotipo_csv("usuariotipo.csv",["andres.david","TL"]))

from archivojson import guardar_json
print(guardar_json('julio.json',{"curso":"python","nivel":"intermedio"}))