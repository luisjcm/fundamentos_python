# Listas se declaran con []
cola_tickets = ["INC-101", "INC-102", "INC-103"]
print(f"Cola inicial: {cola_tickets}")


#1. append(): Agrega un nuevo elemento al final de la lista
cola_tickets.append("INC-104")
print(f"Nuevo ticket reportado: {cola_tickets}")

#2. Acceso por indice: En Python (y casi todo lenguaje), se empieza a contar desde el 0
ticket_actual = cola_tickets[0]
print(f"\n---> Atendiendo el ticket prioritario: {ticket_actual}")

#3. remove(): Busca un elemento por su nombre exacto y lo elimina de la lista
cola_tickets.remove(ticket_actual)
print(f"Ticket resuelto. Cola actualizada: {cola_tickets}")

#4. pop(): Saca y te devuelve el ultimo elemento de la lista (o el índice que le pase)
ticket_cancelado = cola_tickets.pop()
print(f"\nEl usuario canceló el ticket {ticket_cancelado}.")
print(f"Cola final al terminal el turno: {cola_tickets}")