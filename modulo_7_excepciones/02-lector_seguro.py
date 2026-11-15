print("--- INICIANDO SISTEMA DE MONITOREO ---")

archivo_config = "configuracion_red.json"

try:
    # 1. Intentamos abrir un archivo que SABEMOS que no existe en tu carpeta actual
    print(f"Buscando archivo de configuración '{archivo_config}'...")
    with open(archivo_config, "r", encoding="utf-8") as f:
        datos = f.read()
        print("✅ Configuración cargada con éxito.")

except FileNotFoundError:
    # 2. Si el archivo no existe, atrapamos el error y nos auto-reparamos
    print(f"⚠️ ALERTA: No se encontró el archivo '{archivo_config}'.")
    print("🔧 El sistema de auto-reparación está creando un archivo por defecto...")
    
    # Lo creamos usando el modo "w"
    with open(archivo_config, "w", encoding="utf-8") as f:
        f.write('{\n    "ip_servidor": "192.168.1.100",\n    "puerto": 8080\n}')
        
    print("✅ Archivo restaurado exitosamente. Ya puedes reiniciar el sistema.")

except Exception as e:
    # Este bloque atrapa CUALQUIER otro error inesperado (permisos, disco lleno, etc.)
    # La variable 'e' guarda el mensaje original del sistema
    print(f"❌ ERROR CRÍTICO DESCONOCIDO: {e}")

finally:
    print("--- Secuencia de inicio finalizada ---")