import json
import os # Esta librería nos permite interactuar con los archivos del sistema operativo

archivo_db = "tickets_avior.json"
azul_claro = "\033[94m"
verde = "\033[92m"
reset = "\033[0m"

# 1. CARGAR DATOS EXISTENTES
# os.path.exists() verifica si el archivo ya existe en tu disco duro
if os.path.exists(archivo_db):
    with open(archivo_db, "r", encoding="utf-8") as f:
        lista_tickets = json.load(f)
else:
    lista_tickets = [] # Si no existe, empezamos con una lista vacía

# 2. MOSTRAR EL ESTADO ACTUAL
print(f"{azul_claro}--- SISTEMA DE TICKETS AVIOR ---{reset}")
print(f"Tickets actuales en base de datos: {len(lista_tickets)}")
for t in lista_tickets:
    print(f"-> [{t['id']}] {t['asunto']} | Estado: {t['estado']}")

# 3. REGISTRAR UN NUEVO TICKET
print("\n--- Registrar Nuevo Ticket ---")
# Generamos un ID automático basado en cuántos tickets ya existen
nuevo_id = len(lista_tickets) + 1
nuevo_asunto = input("Ingresa el asunto del problema: ")

# Empaquetamos los datos en un diccionario
nuevo_ticket = {
    "id": nuevo_id,
    "asunto": nuevo_asunto,
    "estado": "Abierto"
}

# Lo agregamos a nuestra lista en memoria RAM
lista_tickets.append(nuevo_ticket)

# 4. GUARDAR CAMBIOS EN EL DISCO DURO
with open(archivo_db, "w", encoding="utf-8") as f:
    json.dump(lista_tickets, f, indent=4)

print(f"\n{verde}✅ Ticket #{nuevo_id} registrado y base de datos guardada.{reset}")