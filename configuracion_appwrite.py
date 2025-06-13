# configuracion_appwrite.py

import os
from dotenv import load_dotenv
from appwrite.client import Client
from appwrite.services.databases import Databases

# Cargar variables de entorno desde .env
load_dotenv()

# Configuración del cliente de Appwrite
cliente = Client()

cliente.set_endpoint(os.getenv("APPWRITE_ENDPOINT"))       # Ejemplo: 'https://cloud.appwrite.io/v1'
cliente.set_project(os.getenv("APPWRITE_PROJECT_ID"))      # ID del proyecto
cliente.set_key(os.getenv("APPWRITE_API_KEY"))             # Llave secreta de API

# Instancia del servicio de base de datos
base_datos = Databases(cliente)

# ID de la base de datos y colección
ID_BASE_DATOS = os.getenv("APPWRITE_DATABASE_ID")          # Debes definirlo en tu archivo .env
ID_COLECCION_SOCIOS = os.getenv("APPWRITE_COLECCION_SOCIOS")  # Lo mismo
