<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Partner AI v3.0</title>

<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>

<body>

<div class="container">

    <h1>🤖 Partner AI</h1>

    <div id="core">
        <div id="orb"></div>
    </div>

    <div id="status">
        Ready
    </div>

    <div id="chat"></div>

    <div class="controls">

        <input
        id="textCommand"
        placeholder="Ask Partner anything...">

        <button onclick="sendText()">
            Send
        </button>

    </div>

    <button id="micButton" onclick="voiceCommand()">
        🎤 Speak
    </button>

</div>

<script src="{{ url_for('static', filename='js/app.js') }}"></script>
<script src="{{ url_for('static', filename='js/ai_core.js') }}"></script>

</body>
</html>
