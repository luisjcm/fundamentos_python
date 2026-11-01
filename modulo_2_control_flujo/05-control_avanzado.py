cola_tickets = ["INC-101", "SPAM", "INC-102", "SPAM", "INC-103"]

for ticket in cola_tickets:
    if "SPAM" in ticket: continue
    else: print("Procesando ticket normalmente")