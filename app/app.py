from flask import Flask, request, jsonify
import mysql.connector
import time
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

REQUEST_COUNT = Counter('app_requests_total', 'Total requests')

def get_db():
    for _ in range(10):
        try:
            return mysql.connector.connect(
                host="db",
                user="lamp_user",
                password="StrongPassword123!",
                database="lamp_db"
            )
        except:
            time.sleep(2)
    raise Exception("DB not ready")

@app.route("/")
def home():
    REQUEST_COUNT.inc()
    return "App running"

@app.route("/notes", methods=["GET", "POST"])
def notes():
    REQUEST_COUNT.inc()
    db = get_db()
    cursor = db.cursor()

    if request.method == "POST":
        content = request.json.get("content")
        cursor.execute("INSERT INTO notes (content) VALUES (%s)", (content,))
        db.commit()
        return {"status": "ok"}

    cursor.execute("SELECT content FROM notes")
    return jsonify([row[0] for row in cursor.fetchall()])

from flask import Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)
