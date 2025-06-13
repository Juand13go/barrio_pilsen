# guardar_socio.py

from appwrite.input_file import InputFile
from appwrite.exception import AppwriteException
from configuracion_appwrite import base_datos, ID_BASE_DATOS, ID_COLECCION_SOCIOS
from datetime import datetime
import uuid

def guardar_socio(datos):
    try:
        documento_id = str(uuid.uuid4())  # ID único para cada socio

        respuesta = base_datos.create_document(
            database_id=ID_BASE_DATOS,
            collection_id=ID_COLECCION_SOCIOS,
            document_id=documento_id,
            data={
                "nombre": datos["nombre"],
                "apellido": datos["apellido"],
                "tipo_documento": datos["tipo_documento"],
                "numero_documento": datos["numero_documento"],
                "fecha_nacimiento": datos["fecha_nacimiento"],
                "direccion": datos["direccion"],
                "telefono": datos["telefono"],
                "correo": datos["correo"],
                "fecha_ingreso": datos["fecha_ingreso"],
                "estado": datos["estado"],
                "rol": datos["rol"],
                "fecha_registro": datetime.now().isoformat()
            }
        )
        return {"exito": True, "respuesta": respuesta}
    
    except AppwriteException as error:
        print("Error al guardar socio:", error)
        return {"exito": False, "error": str(error)}
