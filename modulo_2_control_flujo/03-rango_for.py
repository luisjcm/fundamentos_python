for i in range(1, 6): 
    if i == 3:
        print(f"Error: Tiempo de espera agotado para la IP: 192.168.1.3")
    else: 
        print(f"Haciendo ping a la IP: 192.168.1.{i} ... ¡Respuesta Exitosa! ")