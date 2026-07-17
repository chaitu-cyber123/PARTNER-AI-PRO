const SpeechRecognition =
window.SpeechRecognition || window.webkitSpeechRecognition;

const recognition = new SpeechRecognition();

recognition.lang = "en-US";
recognition.interimResults = false;
recognition.maxAlternatives = 1;

// ---------- UI ----------

function setOrb(color) {
    const orb = document.getElementById("orb");
    if (!orb) return;

    orb.style.background = color;
    orb.style.boxShadow =
        `0 0 20px ${color},
         0 0 50px ${color},
         0 0 90px ${color}`;
}

function setStatus(text) {
    const status = document.getElementById("status");
    if (status) status.innerText = text;
}

function addMessage(sender, message) {

    const chat = document.getElementById("chat");

    const div = document.createElement("div");

    div.className = sender;

    div.innerHTML =
        sender === "user"
        ? `👤 <b>You:</b> ${message}`
        : `🤖 <b>Partner:</b> ${message}`;

    chat.appendChild(div);

    chat.scrollTop = chat.scrollHeight;
}

// ---------- Voice ----------

function voiceCommand() {
    setOrb("#00ff66");
    setStatus("Listening...");
    recognition.start();
}

recognition.onresult = function(event) {

    const command = event.results[0][0].transcript;

    sendCommand(command);

};

recognition.onerror = function(event) {

    setOrb("#ff0000");
    setStatus("Speech Error: " + event.error);

    setTimeout(function () {
        setOrb("#00eaff");
        setStatus("Ready");
    }, 2000);

};

// ---------- Text ----------

function sendText() {

    const input = document.getElementById("textCommand");

    const command = input.value.trim();

    if (command === "") return;

    input.value = "";

    sendCommand(command);

}

// ---------- Common ----------

function sendCommand(command) {

    addMessage("user", command);

    setOrb("#ffd000");
    setStatus("Thinking...");

    fetch("/command", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            command: command
        })

    })

    .then(res => res.json())

    .then(data => {

        addMessage("partner", data.response);

        setOrb("#0099ff");
        setStatus("Speaking...");

        window.speechSynthesis.cancel();

        const speech = new SpeechSynthesisUtterance(data.response);

        speech.lang = "en-US";
        speech.rate = 1;
        speech.pitch = 1;

        speech.onend = function () {

            setOrb("#00eaff");
            setStatus("Ready");

        };

        window.speechSynthesis.speak(speech);

    })

    .catch(err => {

        addMessage("partner", "Connection Error");

        console.log(err);

        setOrb("red");
        setStatus("Offline");

    });

}

// ---------- Clock ----------

setInterval(function(){

    const now = new Date();

    document.getElementById("clock").innerText =
        now.toLocaleTimeString();

},1000);

// ---------- Enter Key ----------

document.addEventListener("DOMContentLoaded", function(){

    const input = document.getElementById("textCommand");

    input.addEventListener("keypress", function(e){

        if(e.key==="Enter")
            sendText();

    });

});
