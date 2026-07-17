const SpeechRecognition =
window.SpeechRecognition || window.webkitSpeechRecognition;

if (!SpeechRecognition) {
    alert("Your browser does not support Speech Recognition.");
}

const recognition = new SpeechRecognition();

recognition.lang = "en-US";
recognition.interimResults = false;
recognition.maxAlternatives = 1;

// Change orb color safely
function setOrb(color) {
    const orb = document.getElementById("orb");
    if (!orb) return;

    orb.style.background = color;
    orb.style.boxShadow = "0 0 60px " + color;
}

// Speak button
function voiceCommand() {
    setOrb("#00ff66"); // Listening
    recognition.start();
}

// Speech recognized
recognition.onresult = function(event) {

    setOrb("#ffcc00"); // Thinking

    const command = event.results[0][0].transcript;

    fetch("/command", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            command: command
        })
    })
    .then(response => response.json())
    .then(data => {

        const chat = document.getElementById("chat");

        chat.innerHTML += `
        <div class="user">
            👤 <b>You:</b> ${data.command}
        </div>

        <div class="partner">
            🤖 <b>Partner:</b> ${data.response}
        </div>
        `;

        chat.scrollTop = chat.scrollHeight;

        setOrb("#00bfff"); // Speaking

        window.speechSynthesis.cancel();

        const speech = new SpeechSynthesisUtterance(data.response);

        speech.lang = "en-US";
        speech.rate = 1;
        speech.pitch = 1;

        speech.onend = function () {
            setOrb("#00eaff");
        };

        speech.onerror = function () {
            setOrb("red");
        };

        window.speechSynthesis.speak(speech);

    })
    .catch(error => {

        const chat = document.getElementById("chat");

        chat.innerHTML += `
        <div class="partner">
            ❌ Error: ${error}
        </div>
        `;

        setOrb("red");
    });

};

// Recognition failed
recognition.onerror = function(event) {

    const chat = document.getElementById("chat");

    chat.innerHTML += `
    <div class="partner">
        ❌ Speech Error: ${event.error}
    </div>
    `;

    setOrb("red");
};

// Optional text command support
function sendText() {

    const input = document.getElementById("textCommand");

    if (!input.value.trim()) return;

    fetch("/command", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            command: input.value
        })
    })
    .then(response => response.json())
    .then(data => {

        const chat = document.getElementById("chat");

        chat.innerHTML += `
        <div class="user">
            👤 <b>You:</b> ${data.command}
        </div>

        <div class="partner">
            🤖 <b>Partner:</b> ${data.response}
        </div>
        `;

        chat.scrollTop = chat.scrollHeight;

        input.value = "";

        window.speechSynthesis.cancel();

        const speech = new SpeechSynthesisUtterance(data.response);

        speech.lang = "en-US";

        window.speechSynthesis.speak(speech);

    });

}
