# 🐍 Fundamentos de Python

Este repositorio contiene mi progreso, prácticas y laboratorios para dominar las bases y aplicaciones de Python. El código está estructurado en módulos progresivos para facilitar su lectura y ejecución. Los ejercicios están contextualizados en un escenario de **soporte técnico / mesa de ayuda (IT)**: tickets, inventario de equipos, servidores y configuración de red.

## 📁 Estructura del Repositorio

* **`modulo_1_introduccion/`**: Tipos de datos primitivos, manejo de variables, conversiones y formateo de cadenas (f-strings).
* **`modulo_2_control_flujo/`**: Lógica condicional (`if/elif/else`), bucles `while` controlados, bucles `for` y `match-case`.
* **`modulo_3_funciones/`**: Creación de funciones, parámetros, `return`, alcance de variables (scope), `*args` y `**kwargs`.
* **`modulo_4_estructuras_datos/`**: Listas, métodos nativos (`append`, `pop`, `remove`), diccionarios y listas de diccionarios (simulación de JSON).
* **`modulo_5_manejo_archivos/`**: Lectura, escritura y persistencia de datos en disco con `with open()`: archivos `.txt` (modos `"w"` y `"a"`), archivos `.json` (`json.dump` / `json.load`) y un sistema de tickets que guarda su estado entre ejecuciones.
* **`modulo_6_poo/`**: Programación orientada a objetos: clases y objetos, constructor (`__init__`), métodos, herencia con `super()` y gestión de listas de objetos (por ejemplo, un datacenter de servidores).
* **`modulo_7_excepciones/`**: Manejo de errores con `try/except/else/finally`, captura de excepciones específicas (`FileNotFoundError`) y generales (`Exception`), y un lector de archivos "seguro" con auto-reparación.
* **`modulo_8_apis/`**: Consumo de APIs REST con la librería `requests`: peticiones `GET`, validación del código de estado HTTP, lectura de respuestas JSON y manejo de errores de conexión.
* **`proyecto_final/`**: `app_tickets.py`, un **sistema de tickets** que integra todo lo aprendido: una clase `Ticket` (POO), un técnico obtenido desde una API externa (`requests`), persistencia en `historial_tickets.json` (archivos y JSON) y manejo de errores (excepciones) para continuar funcionando sin internet o sin base de datos.

## 🗂️ Archivos de Datos

Archivos en la raíz que generan y consumen los scripts de los módulos y el proyecto final:

* **`bitacora_soporte.txt`**: Bitácora de soporte en texto plano (módulo 5).
* **`inventario.json`**: Inventario de equipos con IP y estado (módulo 5).
* **`tickets_avior.json`**: Base de datos del sistema de tickets del módulo 5.
* **`configuracion_red.json`**: Configuración de red por defecto, creada por el lector seguro (módulo 7).
* **`historial_tickets.json`**: Base de datos de tickets del proyecto final.

## 🚀 Entorno de Desarrollo

* **Lenguaje:** Python 3.15
* **OS:** Ubuntu Linux
* **Editor:** Visual Studio Code
* **Dependencias externas:** [`requests`](https://pypi.org/project/requests/) (módulo 8 y proyecto final)

## ▶️ Cómo Ejecutar

1. Clona el repositorio e instala la dependencia:

```bash
git clone https://github.com/luisjcm/fundamentos_python.git
cd fundamentos_python
pip install requests
```

2. Ejecuta cualquier script **desde la raíz del repositorio**, para que las rutas relativas a los archivos `.txt` y `.json` funcionen:

```bash
python3 modulo_1_introduccion/00-hola_mundo.py
python3 proyecto_final/app_tickets.py
```

> Los módulos 8 y el proyecto final necesitan conexión a internet para consultar la API de prueba [JSONPlaceholder](https://jsonplaceholder.typicode.com/). Sin conexión, el proyecto final asigna un técnico local y sigue funcionando.

## 👨‍💻 Autor

* **Luis Jesus Curbata** - [https://luisjcm.com/](https://luisjcm.com/)