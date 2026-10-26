tickets = ["INC-5021", "INC-5022", "REQ-8040", "INC-5023"]

for ticket in tickets:
    if "INC" in ticket:
        print(f"🚨 Resolviendo incidente: {ticket}")
    elif "REQ" in ticket:
        print(f"✅ Procesando requerimiento: {ticket}")