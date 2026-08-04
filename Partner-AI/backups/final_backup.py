
from flask import Flask, render_template, request, jsonify

from ai.brain import ask
from skills.router import handle_command

from services.boot import boot_sequence
from services.startup import startup_message
from services.reminder_service import start_reminder_service
import subprocess
import json
import time


app = Flask(
    __name__,
    template_folder="ui/templates",
    static_folder="ui/static"
)



@app.route("/")
def home():

    return render_template(
        "dashboard.html"
    )



@app.route("/boot")
def boot():

    return jsonify({
        "boot": boot_sequence()
    })

def get_cpu_usage():

    try:
        with open("/proc/stat", "r") as f:
            values1 = list(map(int, f.readline().split()[1:]))

        time.sleep(0.1)

        with open("/proc/stat", "r") as f:
            values2 = list(map(int, f.readline().split()[1:]))

        idle = values2[3] - values1[3]
        total = sum(values2) - sum(values1)

        if total == 0:
            return 0

        usage = 100 * (total - idle) / total
        return round(usage, 1)

    except:
        return "N/A"

@app.route("/status")
def status():

    from ai.memory import load_memory


    memory = load_memory()

    count = 0


    for section in memory.values():

        if isinstance(section, dict):

            count += len(section)


        battery = "--"

    try:
        result = subprocess.check_output(
            ["termux-battery-status"],
            text=True
        )

        info = json.loads(result)
        battery = info["percentage"]

    except Exception:
        battery = "--"

    return jsonify({
        "time": time.strftime("%I:%M %p"),
        "cpu": get_cpu_usage(),
        "ram": "N/A",
        "memory": count,
        "network": "ONLINE",
        "battery": battery
    })

@app.route("/listen")
def listen():

    try:

        result = subprocess.check_output(
            [
                "termux-speech-to-text"
            ],
            text=True
        )


        data = json.loads(result)


        return jsonify({

            "text":
            data.get("text", "")

        })


    except Exception as e:

        return jsonify({

            "text": "",

            "error": str(e)

        })



@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json(
        silent=True
    ) or {}


    message = data.get(
        "message",
        ""
    ).strip()


    if not message:

        return jsonify({

            "reply":
            "Please type a message."

        })


    result = handle_command(
        message
    )


    if result is None:

        return jsonify({

            "reply":
            ask(message)

        })


    if isinstance(result, dict):

        return jsonify(result)


    return jsonify({

        "reply":
        result

    })
import os

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/upload", methods=["POST"])
def upload_image():

    if "image" not in request.files:
        return jsonify({
            "success": False,
            "error": "No image received"
        })

    image = request.files["image"]

    path = os.path.join(
        UPLOAD_FOLDER,
        image.filename
    )

    image.save(path)

    prompt = request.form.get(
        "prompt",
        "What do you see in this image?"
    )

    result = ask(
        prompt,
        image_path=path
    )

    return jsonify({
        "success": True,
        "filename": image.filename,
        "analysis": result
    })
@app.route("/notifications")
def notifications():

    import json

    file = "data/notifications.json"

    if not os.path.exists(file):
        return jsonify([])

    with open(file, "r") as f:
        data = json.load(f)

    return jsonify(data)


if __name__ == "__main__":

    start_reminder_service()

    app.run(
    host="0.0.0.0",
    port=5000,
    debug=False
)
