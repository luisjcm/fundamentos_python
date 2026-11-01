verde = "\033[92m"
reset = "\033[0m"
azul_claro = "\033[94m"

def saludar_soporte(nombre):
    print(f"{verde}---Sistema de Ayuda Técnica Avior---")
    print(f"Bienvenido al sistema, {nombre}{reset}")
    print("-------------------------------------------")

saludar_soporte("Luis Jesus")

# ------------------------------------------------------------------------------------------

def calcular_retiro(saldo_actual, monto):
    nuevo_saldo = saldo_actual - monto
    return nuevo_saldo

saldo_disponible = calcular_retiro(1000.0, 250.0)
print(f"Saldo despues del retiro: {saldo_disponible}")
print("-------------------------------------------")

# ------------------------------------------------------------------------------------------

def registrar_ticket(asunto, prioridad= "media"):
    print(f"{azul_claro}Registrando ticket: '{asunto} | Prioridad asignada: {prioridad}{reset} ")

registrar_ticket("Falla de red en oficina", "Alta")
registrar_ticket("Actualización de Software")