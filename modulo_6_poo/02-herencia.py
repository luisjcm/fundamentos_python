# 1. CLASE PADRE (General)
class Empleado:
    def __init__(self, nombre, departamento):
        self.nombre = nombre
        self.departamento = departamento

    def presentarse(self):
        print(f"Hola, soy {self.nombre} del departamento de {self.departamento}.")

# 2. CLASE HIJA (Especializada). Hereda de Empleado poniendo el Padre entre paréntesis
class TecnicoSoporte(Empleado):
    def __init__(self, nombre, departamento, especialidad):
        # super() llama al __init__ del Padre para que él configure el nombre y departamento
        super().__init__(nombre, departamento)
        # Añadimos el atributo exclusivo del hijo
        self.especialidad = especialidad 

    # Añadimos un método exclusivo que los empleados normales no tienen
    def resolver_ticket(self, id_ticket):
        print(f"🔧 {self.nombre} ({self.especialidad}) está resolviendo el ticket #{id_ticket}...")

# --- FLUJO PRINCIPAL ---
print("--- SISTEMA DE RECURSOS HUMANOS ---")

# Creamos un empleado normal
empleado1 = Empleado("Stephanie", "Marketing")
empleado1.presentarse()

print("\n--- DEPARTAMENTO TI ---")
# Creamos tu perfil como Técnico de Soporte
tecnico_ti = TecnicoSoporte("Luis Jesus", "Help Desk", "Servidores y Redes")

# Magia de la herencia: El técnico puede usar el método del Padre
tecnico_ti.presentarse() 

# Y también puede usar su propio método exclusivo de Hijo
tecnico_ti.resolver_ticket(105)

# Si intentaras hacer empleado1.resolver_ticket(105), Python lanzaría un error.