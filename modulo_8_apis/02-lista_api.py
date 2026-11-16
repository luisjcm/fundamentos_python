import requests

print("--- OBTENIENDO LISTA DE USUARIOS DESDE LA NUBE ---")
# La URL apunta a la colección completa
url = "https://jsonplaceholder.typicode.com/users"

try:
    print("Conectando al servidor...")
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        # Como pedimos la colección completa, la API nos devuelve una LISTA de diccionarios
        lista_usuarios = respuesta.json()
        
        print(f"✅ Descarga completada. Se encontraron {len(lista_usuarios)} usuarios.\n")
        
        # Iteramos sobre la lista para extraer datos específicos de cada uno
        for usuario in lista_usuarios:
            nombre = usuario['name']
            # Fíjate cómo entramos a un diccionario anidado para sacar la ciudad
            ciudad = usuario['address']['city'] 
            
            print(f"-> {nombre} | Ubicación: {ciudad}")
            
    else:
        print(f"❌ Error del servidor. Código: {respuesta.status_code}")

except requests.exceptions.ConnectionError:
    print("❌ ERROR CRÍTICO: No hay conexión a internet.")