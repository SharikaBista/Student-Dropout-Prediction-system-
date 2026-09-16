from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"message": "Student Dropout Prediction System API is running."})

@app.route("/api/test")
def test():
    return jsonify({
        "status": "success",
        "message": "Test endpoint is working."
    })

if __name__ == "__main__":
    app.run(debug=True)

    