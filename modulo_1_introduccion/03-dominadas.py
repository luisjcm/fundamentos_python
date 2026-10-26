repeticiones = int(input("¿Cuantas dominadas haces por serie? "))
series = int(input("¿Cuantas series haces por rutina? "))
dias = int(input("¿Cuantos dias a la semana entrenas? "))

total_repeticiones = repeticiones * series
repeticiones_semana = total_repeticiones * dias

print (f"La cantidad de dominadas que haces semanalmente son: {repeticiones_semana}")