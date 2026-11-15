print("--- HERRAMIENTA DE DIAGNÓSTICO DE RED ---")

# try: "Intenta ejecutar este bloque de código"
try:
    paquetes = int(input("¿Cuántos paquetes de ping deseas enviar? (Ingresa un número): "))
    
    latencia_total = 120 # Simulamos 120ms de latencia acumulada
    latencia_promedio = latencia_total / paquetes
    
    print(f"✅ Enviados {paquetes} paquetes. Latencia promedio: {latencia_promedio} ms")

# except: "Si ocurre ESTE error específico, no explotes, haz esto en su lugar"
except ValueError:
    print("❌ ERROR DE USUARIO: ¡Debes ingresar un número entero válido, no texto ni letras!")

except ZeroDivisionError:
    print("❌ ERROR LÓGICO: No puedes enviar 0 paquetes. No se puede dividir por cero.")

# finally: Se ejecuta SIEMPRE al final, sin importar si hubo éxito o error
finally:
    print("--- Diagnóstico finalizado. Cerrando herramienta... ---")