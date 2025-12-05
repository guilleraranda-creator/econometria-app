from flask import Flask, request, jsonify
from flask_cors import CORS

# Crear la app
app = Flask(__name__)

# Activar CORS para permitir peticiones desde cualquier origen
CORS(app)

# Ruta de prueba
@app.route("/", methods=["GET"])
def home():
    return "Backend funcionando correctamente"

# Ruta para el cálculo
@app.route("/square", methods=["POST"])
def square():
    data = request.get_json()
    numero = data.get("number", 0)
    resultado = numero ** 2
    return jsonify({"result": resultado})

# Ejecutar la app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
