from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/square", methods=["POST"])
def square_number():
    data = request.json
    number = data.get("number", None)

    if number is None:
        return jsonify({"error": "No number provided"}), 400

    result = number ** 2
    return jsonify({"result": result})

@app.route("/")
def home():
    return "Backend funcionando correctamente"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
