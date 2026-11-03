def registrar_equipo(nombre, *args, **kwargs): 
    print(f"\n--- Registrando equipo: {nombre} ---")
    print(f"Accesorios sueltos (*args): {args}")
    print(f"Especificaciones (**kwargs): {kwargs}")


registrar_equipo("PC-Operaciones", "Monitor Dell 22", "Teclado Logitech", "Mouse Inalámbrico", RAM="16GB", CPU="Intel i7", Almacenamiento="512GB SSD", ip="192.168.1.100")