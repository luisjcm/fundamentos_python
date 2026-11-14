# Nuestro "Base de Datos" (Lista de Direccionarios)
inventario_red = [
    {"hostname": "LJLT-5480", "ip": "192.168.1.50", "estado": "Operativo"},
    {"hostname": "SRV-BD01", "ip": "10.0.0.5", "estado": "Caído"},
    {"hostname": "PC-SOPORTE", "ip": "192.168.1.100", "estado": "Operativo"}
]

def buscar_equipo(nombre_buscar):
    for equipo in inventario_red:
        # Si el hostname actual coincide con el que buscamos (ignorando mayúsculas/minúsculas)
        if equipo["hostname"].upper() == nombre_buscar.upper():
            print(f"\n✅ Equipo Encontrado:")
            print(f"Hostname: {equipo['hostname']}")
            print(f"IP: {equipo['ip']}")
            print(f"Estado: {equipo['estado']}")
            return 

        # Si el bucle for termina y nunca hizo 'return', significa que no existe
    print(f"\n❌ Error: El equipo '{nombre_buscar}' no existe en el inventario.")

# --- PRUEBAS ---
# 1. Buscamos un equipo que SÍ existe (incluso escribiéndolo en minúsculas)
buscar_equipo("pc-soporte")

# 2. Buscamos un equipo que NO existe
buscar_equipo("LAPTOP-GERENCIA")