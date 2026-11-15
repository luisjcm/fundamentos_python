class Servidor:
    def __init__(self, hostname, ip):
        self.hostname = hostname
        self.ip = ip
        self.estado = "Online" # Todo servidor nace encendido

    def apagar(self):
        self.estado = "Offline"
        print(f"⚠️ ¡ALERTA! El servidor {self.hostname} ({self.ip}) ha sido apagado.")

# 1. Creamos un Datacenter (Lista), pero ahora metemos OBJETOS reales, no diccionarios
datacenter = [
    Servidor("SRV-BD01", "10.0.0.5"),
    Servidor("SRV-WEB01", "10.0.0.10"),
    Servidor("SRV-MAIL", "10.0.0.15")
]

print("--- ESTADO INICIAL DEL DATACENTER ---")
# 2. Recorremos la lista. En cada vuelta, 'server' es un objeto de la clase Servidor
for server in datacenter:
    print(f"[{server.estado}] {server.hostname} - IP: {server.ip}")

print("\n--- SIMULANDO MANTENIMIENTO ---")
# 3. Accedemos al segundo servidor de la lista (índice 1) y disparamos SU propio método
datacenter[1].apagar()

print("\n--- ESTADO ACTUALIZADO DEL DATACENTER ---")
for server in datacenter:
    if server.estado == "Offline":
        print(f"\033[91m[{server.estado}] {server.hostname}\033[0m") # Rojo si está apagado
    else:
        print(f"\033[92m[{server.estado}] {server.hostname}\033[0m") # Verde si está online