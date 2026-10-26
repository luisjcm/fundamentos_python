# Colores para dar formato a la salida en la terminal
rojo = "\033[91m"
verde = "\033[92m"
reset = "\033[0m"  # Esto devuelve el color a la normalidad

while True: 
    http_code = int(input("Ingrese un código HTTP (o escriba 0 para salir):  "))

    if http_code == 0:
        print("Saliendo del analizador...")
        break

    match http_code:
        case 200: print(f"{verde}200: OK - Conexion Exitosa.{reset}")
        case 404: print(f"{rojo}404: Not Found - Recurso no encontrado.{reset}")
        case 500: print(f"{rojo}500: Internal Server Error - Fall en el servidor.{reset}")
        case _: print("Código HTTP desconocido")