const SpeechRecognition =
window.SpeechRecognition || window.webkitSpeechRecognition;

const recognition = new SpeechRecognition();

recognition.lang = "en-US";
recognition.interimResults = false;

function setOrb(color) {
    const orb = document.getElementById("orb");
    orb.style.background = color;
    orb.style.boxShadow = "0 0 60px " + color;
}

function voiceCommand() {
    setOrb("#00ff66"); // Listening
    recognition.start();
}

recognition.onresult = function(event) {

    setOrb("#ffcc00"); // Thinking

    let command = event.results[0][0].transcript;

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

        const speech = new SpeechSynthesisUtterance(data.response);
        speech.lang = "en-US";
        speech.rate = 1;
        speech.pitch = 1;

window.speechSynthesis.cancel();

speech.onstart = function() {
    setOrb("#00bfff"); // Speaking
};

speech.onend = function() {
    setOrb("#00eaff"); // Idle
};

speech.onerror = function() {
    setOrb("#00eaff"); // Idle if speech fails
};

window.speechSynthesis.speak(speech);

setTimeout(function() {
    setOrb("#00eaff");
}, 10000);        
    })

    .catch(error => {

        document.getElementById("result").innerHTML =
            "<b>Error:</b> " + error;

        setOrb("red");
    });
};

recognition.onerror = function(event) {

    document.getElementById("result").innerHTML =
        "<b>Speech Error:</b> " + event.error;

    setOrb("red");
};
