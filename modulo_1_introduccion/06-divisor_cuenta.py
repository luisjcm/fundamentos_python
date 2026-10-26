monto_total_cuenta = float(input("Cual es el total de la cuenta?  "))
porcentaje_propina = float(input("Cual es el porcentaje de propina que desea dejar?  "))
personas = int(input("Cuantas personas van a pagar la cuenta?  "))

propina = monto_total_cuenta * (porcentaje_propina / 100)
total_con_propina = monto_total_cuenta + propina
total_por_persona = total_con_propina / personas

print (f"El gran total a pagar con propina es: ${total_con_propina:.2f}. Dividido entre {personas} personas, cada uno debe pagar: ${total_por_persona:.2f}")