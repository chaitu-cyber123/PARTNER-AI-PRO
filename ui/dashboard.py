import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, render_template, request, jsonify
from commands import handle_command
from ai import ask

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("dashboard.html")


@app.route("/command", methods=["POST"])
def command():
    data = request.get_json()

    command = data.get("command", "")

    response = handle_command(command)
    print("Built-in response:", response)

    if response is None:
        print("Calling AI...")
        response = ask(command)

    print("Final response:", response)

    return jsonify({
        "command": command,
        "response": response
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
