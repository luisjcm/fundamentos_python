verde = "\033[92m"
rojo = "\033[91m"
azul_claro = "\033[94m"
reset = "\033[0m"

def consultar_saldo(saldo):
    print(f"{azul_claro}Tu saldo actual es: ${saldo}{reset}")

def depositar(saldo, monto):
    if monto > 0:
        nuevo_saldo = saldo + monto
        print(f"{verde}Deposito exitoso. Has depositado: ${monto}{reset}")
        return nuevo_saldo
    else: 
        print(f"{rojo}Error: El monto debe ser mayor a 0.{reset}")
        return saldo

def retirar(saldo, monto):
    if monto > saldo:
        print(f"{rojo}Error: Fondos insuficientes.{reset}")
        return saldo
    elif monto <= 0:
        print(f"{rojo}Error: El monto debe ser mayor a 0.{reset}")
        return saldo
    else:
        nuevo_saldo = saldo - monto
        print(f"{verde}Retiro exitoso. Has retirado: ${monto}{reset}")
        return nuevo_saldo

#---Flujo principal del programa---
saldo_cuenta = 1000.0

while True:
    print(f"\n{azul_claro}--- Cajero Automatico Avior ---{reset}")
    print("1. Consultar Saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("0. SALIR")

    opcion = int(input("\nSelecciona una opcion: "))

    match opcion:
        case 1:
            consultar_saldo(saldo_cuenta)
        case 2:
            ingreso = float(input("Monto a depositar: "))
            saldo_cuenta = depositar(saldo_cuenta, ingreso)
        case 3: 
            egreso = float(input("Monto a retirar: "))
            saldo_cuenta = retirar(saldo_cuenta, egreso)
        case 0:
            print(f"{verde}Gracias por usar el Cajero. Hasta pronto! {reset}")
            break
        case _:
            print(f"{rojo}Opcion no valida. Intenta de nuevo. {reset}")

