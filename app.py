from flask import Flask, render_template, request, jsonify
from ai.brain import ask

app = Flask(
    __name__,
    template_folder="ui/templates",
    static_folder="ui/static"
)

@app.route("/")
def home():
    return render_template("dashboard.html")

@app.route("/command", methods=["POST"])
def command():

    data = request.get_json()

    command = data.get("command", "")

    response = ask(command)

    return jsonify({
        "command": command,
        "response": response
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

