pin_correcto = "1234"
intentos = 3

while intentos > 0: 
    pin_ingresado = input("Ingrese su PIN de 4 digitos: ")

    if pin_ingresado == pin_correcto:
        print("PIN correcto. Acceso concedido.")
        break
    else:
        intentos -= 1
        print(f"PIN incorrecto. Te quedan {intentos} intentos.")

if intentos == 0:
    print("Cuenta bloqueada por seguridad. Contacte a su banco.")