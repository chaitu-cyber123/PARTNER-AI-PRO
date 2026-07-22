from flask import Flask, render_template, request, jsonify
from ai.brain import ask
import subprocess
import json
from skills.router import handle_command
from services.startup import startup_message
from services.boot import boot_sequence
app = Flask(
    __name__,
    template_folder="ui/templates",
    static_folder="ui/static"
)

@app.route("/")
def home():
    return render_template("dashboard.html")
@app.route("/listen")
def listen():
    try:
        result = subprocess.check_output(
            ["termux-speech-to-text"],
            text=True
        )

        data = json.loads(result)

        return jsonify({
            "text": data.get("text", "")
        })

    except Exception as e:
        return jsonify({
            "text": "",
            "error": str(e)
        })
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "").strip()

    if not message:
        return jsonify({"reply": "Please type a message."})

    result = handle_command(message)

    if result is None:
        return jsonify({"reply": ask(message)})

    if isinstance(result, dict):
        return jsonify(result)

    return jsonify({"reply": result})
@app.route("/boot")
def boot():
    return jsonify({
        "boot": boot_sequence()
    })@app.route("/status")
def status():

    from ai.memory import load_memory
    import time
    import os


    memory = load_memory()

    count = 0

    for section in memory.values():
        if isinstance(section, dict):
            count += len(section)


    # RAM from Android Linux system
    ram_usage = "N/A"

    try:
        with open("/proc/meminfo") as f:
            meminfo = f.read()

        total = int(
            meminfo.split("MemTotal:")[1]
            .split()[0]
        )

        available = int(
            meminfo.split("MemAvailable:")[1]
            .split()[0]
        )

        used = total - available

        ram_usage = round(
            (used / total) * 100,
            1
        )

    except:
        pass


    return jsonify({

        "time": time.strftime("%I:%M %p"),

        "cpu": "ONLINE",

        "ram": ram_usage,

        "memory": count,

        "network": "ONLINE"

    })
if __name__ == "__main__": app.run(host="0.0.0.0", 
       port=5000)
