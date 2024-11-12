from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/message', methods=['POST'])
def message():
    user_message = request.json.get("message")
    ai_reply = f"Respuesta de IA para: '{user_message}'"  # Sustituye esto por tu lógica de IA real
    return jsonify({"reply": ai_reply})

if __name__ == '__main__':
    app.run(debug=True)
