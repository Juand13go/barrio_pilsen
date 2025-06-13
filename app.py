# app.py

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from guardar_socio import guardar_socio

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/registrar-socio", methods=["POST"])
def registrar_socio():
    datos = request.json

    campos_obligatorios = [
        "nombre", "apellido", "tipo_documento", "numero_documento",
        "fecha_nacimiento", "direccion", "telefono", "fecha_ingreso",
        "estado", "rol"
    ]

    for campo in campos_obligatorios:
        if campo not in datos or not datos[campo].strip():
            return jsonify({"exito": False, "error": f"Falta el campo obligatorio: {campo}"}), 400

    resultado = guardar_socio(datos)

    if resultado["exito"]:
        return jsonify({"exito": True, "mensaje": "Socio registrado correctamente."}), 201
    else:
        return jsonify({"exito": False, "error": resultado["error"]}), 500

if __name__ == "__main__":
    app.run(debug=True)
