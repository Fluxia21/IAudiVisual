import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})  # luego cerramos a tu dominio

@app.get("/health")
def health():
    return jsonify({"status": "ok"})

@app.get("/")
def root():
    return jsonify({"msg": "API IAudioVisual OK"})

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
