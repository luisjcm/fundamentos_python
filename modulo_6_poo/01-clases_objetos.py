# Definimos nuestra "Plantilla" o "Molde" con la palabra class (siempre en mayúscula inicial)
class Ticket : 


    # El método __init__ es el "Constructor". Se ejecuta automáticamente cada vez que creamos un ticket nuevo.
    def __init__(self, id_ticket, asunto, usuario):
        self.id = id_ticket
        self.asunto = asunto
        self.usuario = usuario
        self.estado = "Abierto"

    # Un "Método" es una función que vive dentro de la clase. Define lo que el objeto puede "hacer".
    def mostrar_resumen(self):
        azul_claro = "\033[94m"
        reset = "\033[0m"
        print(f"{azul_claro}Ticket #{self.id} | {self.usuario}{reset} -> {self.asunto} ({self.estado})")

        # Nuevo método para cerrar el ticket
    def cerrar_ticket(self):
        self.estado = "Cerrado"  # El objeto se cambia el estado a SÍ MISMO
        print(f"\n✅ El ticket #{self.id} ha sido cerrado por el sistema.")


# ---Flujo Principal ---

print("--- FABRICANDO OBJETOS ---")

# 1. Usamos el molde (Clase) para instanciar (fabricar) dos Objetos reales e independientes
ticket1 = Ticket(101, "Falla de red en mostrador", "Luis Jesus")
ticket2 = Ticket(102, "Error al imprimir boarding pass", "Daniel Gonzalez")

# 2. Cada objeto tiene vida propia. Les ordenamos que ejecuten su propia acción:
ticket1.mostrar_resumen()
ticket2.mostrar_resumen()

# 3. Ordenamos a ticket1 que cambie su estado a SÍ MISMO
ticket1.cerrar_ticket()
ticket1.mostrar_resumen()  # Lo volvemos a imprimir para confirmar el cambio