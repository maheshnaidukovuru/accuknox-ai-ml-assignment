from flask import Flask, jsonify
import json
from pathlib import Path

app = Flask(__name__)
DATA_FILE = Path(__file__).parent / "students.json"

@app.route("/api/students", methods=["GET"])
def get_students():
    with DATA_FILE.open("r", encoding="utf-8") as file:
        students = json.load(file)
    return jsonify(students)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)