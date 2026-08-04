const input =
document.getElementById("message");


const chat =
document.getElementById("chat-box");


const orb = document.getElementById("orb");
function stopSpeaking(){

    speechSynthesis.cancel();

    setOrbState("idle");

}
function setOrbState(state){
    if(!orb) return;

    orb.classList.remove(
        "idle",
        "listening",
        "thinking",
        "speaking"
    );
const listen = document.getElementById("listen-state");
const think = document.getElementById("think-state");
const response = document.getElementById("response-state");

if(listen)
    listen.textContent =
        "LISTENING : " + (state==="listening" ? "TRUE" : "FALSE");

if(think)
    think.textContent =
        "THINKING : " + (state==="thinking" ? "TRUE" : "FALSE");

if(response)
    response.textContent =
        "STATUS : " + state.toUpperCase();
    orb.classList.add(state);
}
function addMessage(sender, text){


    const msg =
    document.createElement("p");


    msg.innerHTML =
    `<b>${sender}:</b> ${text}`;


    chat.appendChild(msg);


    chat.scrollTop =
    chat.scrollHeight;


}



async function sendMessage(){

    const message = input.value.trim();

    if(message === ""){
        return;
    }

    // Stop speech immediately
    if(message.toLowerCase() === "stop"){

        speechSynthesis.cancel();

        setOrbState("idle");

        addMessage("YOU","Stop");

        input.value="";

        return;
    }

    // Cancel any previous speech before asking a new question
    speechSynthesis.cancel();

    addMessage("YOU", message);

    input.value="";

    ...
}


    addMessage("YOU", message);


    input.value="";



    try{

setOrbState("thinking");
        const response =
        await fetch("/chat",{


            method:"POST",


            headers:{


                "Content-Type":
                "application/json"


            },


            body:JSON.stringify({


                message:message


            })


        });


setOrbState("speaking");
     const data = await response.json();

addMessage(
    "PARTNER",
    data.reply || "READY"
);

if (data.action === "open_url") {
    window.open(data.url, "_blank");
}
// Speak through the browser
speechSynthesis.cancel();
const speech = new SpeechSynthesisUtterance(
    data.reply || "READY"
);
speechSynthesis.cancel();
speechSynthesis.speak(speech);
setTimeout(()=>{
    setOrbState("idle");
},1500);


    }


    catch(error){

        addMessage(

            "SYSTEM",

            "CONNECTION ERROR"

        );

setOrbState("idle");
    }


}





if(input){


    input.addEventListener(

    "keydown",

    function(event){


        if(event.key === "Enter"){


            sendMessage();


        }


    });


}
const SpeechRecognition =
    window.SpeechRecognition || window.webkitSpeechRecognition;

if (SpeechRecognition) {

    const recognition = new SpeechRecognition();

    recognition.lang = "en-US";
    recognition.interimResults = false;
    recognition.continuous = false;

    const micBtn = document.getElementById("mic-btn");

    micBtn.addEventListener("click", () => {
        setOrbState("listening");
        recognition.start();
    });

    recognition.onresult = (event) => {
        input.value = event.results[0][0].transcript;
        sendMessage();
    };

    recognition.onend = () => {
        setOrbState("idle");
    };

    recognition.onerror = () => {
        setOrbState("idle");
    };

} else {

    alert("Speech Recognition is not supported in this browser.");

}
async function loadCoreStatus(){

    try{

        const response =
        await fetch("/chat",{
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify({
                message:"partner status"
            })
        });


        const data =
        await response.json();


        const panel =
        document.getElementById("core-status");


        if(panel){
            panel.textContent = data.reply;
        }

    }

    catch(error){

        console.log(error);

    }

}


window.addEventListener(
    "load",
    loadCoreStatus
);
async function updateCoreStatus(){

    try{

        const response =
        await fetch("/status");

        const data =
        await response.json();


        const cpu =
        document.getElementById("cpu");

        const ram =
        document.getElementById("ram");
const battery =
document.getElementById("battery");

        const clock =
        document.getElementById("clock");

        const clock2 =
        document.getElementById("clock2");

        const mobileClock =
        document.getElementById("clock-mobile");


        if(cpu)
            cpu.textContent = data.cpu + "%";


        if(ram)
            ram.textContent = data.ram + "%";
if(battery)
    battery.textContent = data.battery + "%";

        if(clock)
            clock.textContent = data.time;


        if(clock2)
            clock2.textContent = data.time;


        if(mobileClock)
            mobileClock.textContent = data.time;


    }

    catch(error){

        console.log(
            "STATUS UPDATE ERROR",
            error
        );

    }

}


setInterval(
    updateCoreStatus,
    3000
);


updateCoreStatus();
let lastNotificationTime = "";
async function checkNotifications(){

    try{

        const response = await fetch("/notifications");
        const data = await response.json();

        if(data.length > 0){

    const latest = data[data.length - 1];

    if(latest.time !== lastNotificationTime){

        lastNotificationTime = latest.time;

        addMessage(
            "🔔 PARTNER",
            latest.message
        );

        const speech =
        new SpeechSynthesisUtterance(
            latest.message
        );

        speech.rate = 1;
        speech.pitch = 1;

        speechSynthesis.speak(speech);
    }
}

    }
    catch(error){

        console.log(
            "NOTIFICATION ERROR",
            error
        );

    }

}


setInterval(
    checkNotifications,
    5000
);

async function uploadImage() {

    const input = document.getElementById("image-input");

    if (!input.files.length) return;

    const file = input.files[0];

    const formData = new FormData();
    formData.append("image", file);

    const messageInput = document.getElementById("message");

    let question = messageInput.value.trim();

    if (question === "") {
        question = "What do you see in this image?";
    }

    formData.append("prompt", question);

    const imageURL = URL.createObjectURL(file);

    addMessage(
        "👤 YOU",
        `<br><img src="${imageURL}" class="chat-image">`
    );

    addMessage(
        "👁️ PARTNER",
        "Thinking..."
    );

    try {

        const response = await fetch("/upload", {
            method: "POST",
            body: formData
        });

        const result = await response.json();

        addMessage(
            "👁️ PARTNER",
            result.analysis || "Image received"
        );

        const speech = new SpeechSynthesisUtterance(
            result.analysis || "Image received"
        );

        speechSynthesis.speak(speech);

        messageInput.value = "";
        input.value = "";

    } catch (error) {

        console.error("IMAGE ERROR", error);

        addMessage(
            "SYSTEM",
            "Image upload failed."
        );
    }
}
