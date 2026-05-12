import time

from flask import Flask, Response, jsonify
import psutil

app = Flask(__name__)
START_TIME = time.time()


def get_system_metrics():
    return psutil.cpu_percent(), psutil.virtual_memory().percent

@app.route('/')
def home():
    return jsonify({"status": "running", "service": "devops-api"})

@app.route('/health')
def health():
    cpu, mem = get_system_metrics()
    return jsonify({
        "cpu_percent": cpu,
        "memory_percent": mem,
        "uptime_seconds": int(time.time() - START_TIME),
        "status": "healthy" if cpu < 80 and mem < 80 else "unhealthy"
    })

@app.route('/metrics')
def metrics():
    cpu, mem = get_system_metrics()
    return Response(f"""# HELP app_cpu_percent CPU usage percentage
# TYPE app_cpu_percent gauge
app_cpu_percent {cpu}
# HELP app_memory_percent Memory usage percentage
# TYPE app_memory_percent gauge
app_memory_percent {mem}
""", mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
