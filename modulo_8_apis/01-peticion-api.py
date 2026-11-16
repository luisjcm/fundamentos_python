# Importamos la librería de terceros que acabamos de instalar
import requests

print("--- CONECTANDO AL SISTEMA EXTERNO ---")

# Esta es la dirección de la API (Endpoint) que nos devolverá los datos del usuario 1
url = "https://jsonplaceholder.typicode.com/users/1"

try:
    # requests.get() hace exactamente lo mismo que tu navegador cuando entras a una web
    respuesta = requests.get(url)

    # El código 200 es el estándar universal de internet para "Todo salió perfecto (OK)"
    if respuesta.status_code == 200:
        print("✅ Conexión exitosa. Descargando datos...\n")
        
        # La API nos devuelve un JSON de internet, y esta función lo transforma 
        # automáticamente a un Diccionario de Python
        datos_usuario = respuesta.json()
        
        # Como ya es un diccionario, extraemos las llaves que nos interesan
        print(f"👤 Nombre: {datos_usuario['name']}")
        print(f"📧 Correo: {datos_usuario['email']}")
        print(f"🏢 Empresa: {datos_usuario['company']['name']}")
        
    else:
        # Si la URL estuviera mal (ej: error 404), caería aquí
        print(f"❌ Error en la conexión. Código de estado: {respuesta.status_code}")

except requests.exceptions.ConnectionError:
    # Si te quedas sin WiFi o el cable de red se desconecta, atrapamos la explosión
    print("❌ ERROR CRÍTICO: No hay conexión a internet o el servidor está caído.")