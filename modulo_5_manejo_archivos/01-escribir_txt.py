# 1. Modo "w" (Write): Creamos el archivo (o lo sobreescribimos si existe)
# Nota: \n significa "salto de línea" (Enter). write() no lo hace automáticamente como print().
with open("bitacora_soporte.txt", "w", encoding="utf-8") as archivo:
    archivo.write("--- BITÁCORA DE SOPORTE AVIOR ---\n")
    archivo.write("Fecha: Hoy | Turno: Mañana\n")
    archivo.write("---------------------------------\n")

print("✅ Archivo creado exitosamente.")

# 2. Modo "a" (Append): Agregamos una nueva línea sin borrar el encabezado
nuevo_ticket = "INC-105: Reinicio de router principal."

with open("bitacora_soporte.txt", "a", encoding="utf-8") as archivo:
    archivo.write(f"NUEVO EVENTO: {nuevo_ticket}\n")

print("✅ Evento agregado a la bitácora.")