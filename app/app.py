from flask import Flask, request, jsonify, Response
import mysql.connector
import time

from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# -----------------------
# PROMETHEUS METRICS
# -----------------------

REQUEST_COUNT = Counter(
    'app_requests_total',
    'Total HTTP Requests',
    ['method', 'endpoint']
)

REQUEST_LATENCY = Histogram(
    'app_request_latency_seconds',
    'Request latency per endpoint',
    ['endpoint']
)

# -----------------------
# DATABASE CONNECTION
# -----------------------

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

# -----------------------
# PROMETHEUS ENDPOINT
# -----------------------

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

# -----------------------
# MIDDLEWARE (METRICS AUTO TRACKING)
# -----------------------

@app.before_request
def start_timer():
    request.start_time = time.time()


@app.after_request
def record_metrics(response):
    try:
        if request.path:

            latency = time.time() - request.start_time

            REQUEST_COUNT.labels(
                request.method,
                request.path
            ).inc()

            REQUEST_LATENCY.labels(
                request.path
            ).observe(latency)

    except:
        pass

    return response

# -----------------------
# ROUTES
# -----------------------

@app.route("/")
def home():
    return "App running"

@app.route("/notes", methods=["GET", "POST"])
def notes():
    db = get_db()
    cursor = db.cursor()

    if request.method == "POST":
        content = request.json.get("content")
        cursor.execute("INSERT INTO notes (content) VALUES (%s)", (content,))
        db.commit()
        return jsonify({"status": "created"})

    cursor.execute("SELECT * FROM notes")
    rows = cursor.fetchall()

    return jsonify(rows)

# -----------------------
# RUN
# -----------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
