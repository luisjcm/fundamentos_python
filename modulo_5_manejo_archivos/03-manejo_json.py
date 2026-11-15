import json  # Importamos la librería nativa de Python para manejar JSON

# Nuestra estructura de datos compleja (Lista de Diccionarios)
inventario_glpi = [
    {"id": 1, "equipo": "PC-Operaciones", "ip": "192.168.1.50", "estado": "Operativo"},
    {"id": 2, "equipo": "Router-Principal", "ip": "192.168.1.1", "estado": "Alerta"}
]

print("1. Guardando datos en archivo JSON...")
# Modo "w" para escribir. Usamos json.dump() para transformar la lista de Python a formato JSON
with open("inventario.json", "w", encoding="utf-8") as archivo:
    # indent=4 le da un formato bonito y legible con saltos de línea y espacios
    json.dump(inventario_glpi, archivo, indent=4) 

print("✅ Archivo 'inventario.json' creado exitosamente.\n")


print("2. Leyendo datos desde el archivo JSON...")
# Modo "r" para leer. Usamos json.load() para transformar el JSON de vuelta a una lista de Python
with open("inventario.json", "r", encoding="utf-8") as archivo:
    datos_recuperados = json.load(archivo)

# Comprobamos que sigue siendo una lista de diccionarios funcional
for equipo in datos_recuperados:
    print(f"-> Analizando {equipo['equipo']}... Estado: {equipo['estado']}")