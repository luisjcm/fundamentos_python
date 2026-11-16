import json
import os
import requests

# 1. PROGRAMACIÓN ORIENTADA A OBJETOS (El Molde)
class Ticket:
    def __init__(self, id_ticket, asunto, tecnico):
        self.id = id_ticket
        self.asunto = asunto
        self.tecnico = tecnico
        self.estado = "Abierto"
    
    # Método para convertir el objeto en un diccionario (necesario para guardarlo en JSON)
    def a_diccionario(self):
        return {
            "id": self.id,
            "asunto": self.asunto,
            "tecnico": self.tecnico,
            "estado": self.estado
        }

# 2. CONSUMO DE APIS (Obtener técnico de la nube)
def obtener_tecnico_api(id_usuario):
    url = f"https://jsonplaceholder.typicode.com/users/{id_usuario}"
    try:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            return datos['name']
        else:
            return "Técnico Local (API caída)"
    except requests.exceptions.ConnectionError:
        return "Técnico Local (Sin Internet)"

# --- FLUJO PRINCIPAL ---
print("--- SISTEMA INTELIGENTE DE TICKETS AVIOR ---")
archivo_db = "historial_tickets.json"
tickets_guardados = []

# 3. MANEJO DE ARCHIVOS Y EXCEPCIONES (Cargar BD)
try:
    if os.path.exists(archivo_db):
        with open(archivo_db, "r", encoding="utf-8") as f:
            tickets_guardados = json.load(f)
        print(f"✅ Base de datos local cargada. Tickets previos: {len(tickets_guardados)}")
except Exception as e:
    print(f"⚠️ Advertencia al leer BD: {e}")

# 4. LÓGICA DEL PROGRAMA (Interacción)
asunto_nuevo = input("\nIngresa el problema a reportar: ")
id_nuevo = len(tickets_guardados) + 1

print("\nBuscando técnico disponible en la nube...")
# Simulamos buscar al técnico #3 en la API
nombre_tecnico = obtener_tecnico_api(3) 

# Fabricamos el Objeto Inteligente
nuevo_ticket = Ticket(id_nuevo, asunto_nuevo, nombre_tecnico)

# Lo agregamos a nuestra lista convirtiéndolo a diccionario
tickets_guardados.append(nuevo_ticket.a_diccionario())

# 5. PERSISTENCIA (Guardar cambios)
with open(archivo_db, "w", encoding="utf-8") as f:
    json.dump(tickets_guardados, f, indent=4)

print(f"\n✅ ¡Éxito! Ticket #{nuevo_ticket.id} ('{nuevo_ticket.asunto}') asignado a: {nuevo_ticket.tecnico}")
print("💾 Base de datos actualizada en el disco duro.")