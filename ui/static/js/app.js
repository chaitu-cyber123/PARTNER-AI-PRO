const input = document.getElementById("message");
const chat = document.getElementById("chat-box");
const orb = document.getElementById("orb");

let currentSpeech = null;


function setOrbState(state){

    if(!orb) return;

    orb.classList.remove(
        "idle",
        "listening",
        "thinking",
        "speaking"
    );

    orb.classList.add(state);


    const listen = document.getElementById("listen-state");
    const think = document.getElementById("think-state");
    const response = document.getElementById("response-state");


    if(listen)
        listen.textContent =
        "LISTENING : " + (state==="listening" ? "TRUE":"FALSE");


    if(think)
        think.textContent =
        "THINKING : " + (state==="thinking" ? "TRUE":"FALSE");


    if(response)
        response.textContent =
        "STATUS : " + state.toUpperCase();
}



function stopSpeaking(){

    if(window.speechSynthesis){

        speechSynthesis.pause();

        speechSynthesis.cancel();

        speechSynthesis.resume();

    }

    currentSpeech = null;

    setOrbState("idle");
}


function speak(text){

    speechSynthesis.pause();
    speechSynthesis.cancel();

    currentSpeech =
    new SpeechSynthesisUtterance(text);

    speechSynthesis.resume();

    currentSpeech.rate = 1;
    currentSpeech.pitch = 1;


    currentSpeech.onstart = ()=>{

        setOrbState("speaking");

    };


    currentSpeech.onend = ()=>{

        setOrbState("idle");

    };


    speechSynthesis.speak(currentSpeech);

}



function addMessage(sender,text){

    if(!chat) return;


    const msg =
    document.createElement("p");


    msg.innerHTML =
    `<b>${sender}:</b> ${text}`;


    chat.appendChild(msg);


    chat.scrollTop =
    chat.scrollHeight;

}




async function sendMessage(){

    const message =
    input.value.trim();


    if(message === ""){
        return;
    }


    // instant stop command

    if(message.toLowerCase() === "stop"){
        console.log("STOP COMMAND RECEIVED");
        stopSpeaking();

        addMessage(
            "YOU",
            "Stop"
        );

        input.value="";

        return;
    }


    // New question interrupts old answer

    stopSpeaking();


    addMessage(
        "YOU",
        message
    );


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



        const data =
        await response.json();



        addMessage(
            "PARTNER",
            data.reply || "READY"
        );



        if(data.action === "open_url"){

            window.open(
                data.url,
                "_blank"
            );

        }


        speak(
            data.reply || "READY"
        );



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

            if(event.key==="Enter"){

                sendMessage();

            }

        }
    );

}





// Voice Recognition


const SpeechRecognition =
window.SpeechRecognition ||
window.webkitSpeechRecognition;



if(SpeechRecognition){


    const recognition =
    new SpeechRecognition();


    recognition.lang =
    "en-US";


    recognition.interimResults =
    false;


    recognition.continuous =
    false;



    const micBtn =
    document.getElementById("mic-btn");



    if(micBtn){

        micBtn.addEventListener(
            "click",
            ()=>{


                stopSpeaking();


                setOrbState(
                    "listening"
                );


                recognition.start();


            }
        );

    }




    recognition.onresult =
    (event)=>{


        input.value =
        event.results[0][0].transcript;


        sendMessage();


    };



    recognition.onend =
    ()=>{

        setOrbState("idle");

    };


    recognition.onerror =
    ()=>{

        setOrbState("idle");

    };

}
// Core Status

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
        document.getElementById(
            "core-status"
        );


        if(panel){

            panel.textContent =
            data.reply;

        }


    }

    catch(error){

        console.log(
            "STATUS ERROR",
            error
        );

    }

}




window.addEventListener(
    "load",
    loadCoreStatus
);




// System Status Panel


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
        document.getElementById(
            "clock-mobile"
        );



        if(cpu)
            cpu.textContent =
            data.cpu + "%";


        if(ram)
            ram.textContent =
            data.ram + "%";


        if(battery)
            battery.textContent =
            data.battery + "%";


        if(clock)
            clock.textContent =
            data.time;


        if(clock2)
            clock2.textContent =
            data.time;


        if(mobileClock)
            mobileClock.textContent =
            data.time;



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




// Notifications


let lastNotificationTime = "";



async function checkNotifications(){


    try{


        const response =
        await fetch(
            "/notifications"
        );


        const data =
        await response.json();



        if(data.length > 0){


            const latest =
            data[data.length-1];



            if(
                latest.time !==
                lastNotificationTime
            ){


                lastNotificationTime =
                latest.time;



                addMessage(
                    "🔔 PARTNER",
                    latest.message
                );



                speak(
                    latest.message
                );

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






// Image Upload


async function uploadImage(){


    const imageInput =
    document.getElementById(
        "image-input"
    );


    if(
        !imageInput.files.length
    ){

        return;

    }



    stopSpeaking();



    const file =
    imageInput.files[0];



    const formData =
    new FormData();



    formData.append(
        "image",
        file
    );



    const messageInput =
    document.getElementById(
        "message"
    );



    let question =
    messageInput.value.trim();



    if(question===""){

        question =
        "What do you see in this image?";

    }



    formData.append(
        "prompt",
        question
    );



    const imageURL =
    URL.createObjectURL(file);



    addMessage(
        "👤 YOU",
        `<br><img src="${imageURL}" class="chat-image">`
    );



    addMessage(
        "👁️ PARTNER",
        "Thinking..."
    );



    try{


        const response =
        await fetch(
            "/upload",
            {
                method:"POST",
                body:formData
            }
        );



        const result =
        await response.json();



        const answer =
        result.analysis ||
        "Image received";



        addMessage(
            "👁️ PARTNER",
            answer
        );



        speak(answer);



        messageInput.value="";

        imageInput.value="";



    }


    catch(error){


        addMessage(
            "SYSTEM",
            "Image upload failed."
        );


        console.log(
            error
        );

    }

}
