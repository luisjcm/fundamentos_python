# Diccionarios se declaran con llaves {} y formato clave: valor

equipo_ti = {
    "hostname" : "LJLT-5480",
    "ip": "192.168.1.50",
    "sistema_operativo" : "Ubuntu 26.04 LTS",
    "estado": "operativo"
}

# 1. Acceder a un valor específico usando su clave
print(f"Haciendo ping a: {equipo_ti['ip']}...")

# 2. Modificar un valor existente 
equipo_ti["estado"] = "En Reparacion"
print(f"Nuevo estado: {equipo_ti['estado']}")

# 3. Agregar una nueva clave que no existía (Asignamos el equipo)
equipo_ti["usuario_asignado"] = "Luis Jesus"

# Imprimimos el diccionario completo para ver la estructura final
print("\n--- Ficha Técnica Actualizada ---")
print(equipo_ti)