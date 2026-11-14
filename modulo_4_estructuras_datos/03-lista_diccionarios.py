rojo = "\033[91m"
verde = "\033[92m"
reset = "\033[0m"


# Una lista [] que contiene multiples diccionarios {}

inventario_red = [
    {"hostname" : "LJLT-5480", "ip" : "192.168.1.50", "estado" : "Operativo"},
    {"hostname" : "SRV-BD01", "ip" : "10.0.0.5", "estado" : "Caído"},
    {"hostname" : "PC-SOPORTE", "ip" : "192.168.1.100", "estado" : "Operativo"}
]

print("--- Iniciando Escaneo de Red ---")

# Recorremos la lista. En cada iteración, 'equipo' será un diccionario completo

for equipo in inventario_red:
    if equipo["estado"] == "Caído":
        print(f"{rojo}¡ALERTA CRÍTICA! El equipo {equipo['hostname']} ({equipo['ip']}) no responde.{reset}")
    else:
        print(f"{verde}[OK] Ping exitoso a {equipo['hostname']} ({equipo['ip']}).{reset}")