azul_claro = "\033[94m"
reset = "\033[0m"

# Modo "r" (Read): Abre el archivo estrictamente para lectura
with open("bitacora_soporte.txt", "r", encoding="utf-8") as archivo:
    # .read() extrae TODO el contenido del archivo como un solo bloque de texto string
    contenido_completo = archivo.read()

print(f"{azul_claro}--- LEYENDO LA BITÁCORA DESDE EL DISCO DURO ---{reset}")
print(contenido_completo)