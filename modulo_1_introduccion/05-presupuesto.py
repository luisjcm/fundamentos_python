horas_estimadas = float(input("Ingrese la cantidad de horas estimadas para completar el proyecto: "))
tarifa_por_hora = float(input("Ingrese la tarifa por hora: "))

sub_total = horas_estimadas * tarifa_por_hora
impuesto = sub_total * 0.16
costo_total = sub_total + impuesto

print(f"El subtotal del proyecto es: ${sub_total:.2f}, los impuestos son: ${impuesto:.2f}, y el costo total del proyecto es: ${costo_total:.2f}")