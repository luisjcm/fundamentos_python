nombre_completo = input("Ingrese su nombre completo: ")
numero_telefono = input("Ingrese su número de teléfono: ")

# Se usa strip() para eliminar espacios en blanco al inicio y al final del nombre, y title() para capitalizar la primera letra de cada palabra
nombre_completo = nombre_completo.strip().title()

#Se usa replace() para eliminar caracteres no deseados del número de teléfono, como guiones, espacios y paréntesis
numero_telefono = numero_telefono.replace("-", "").replace(" ", "").replace("(", "").replace(")", "")

print(f"Nombre completo: {nombre_completo}")
print(f"Número de teléfono: {numero_telefono}")
print(f"Cantidad de caracteres en el nombre completo: {len(nombre_completo)}")