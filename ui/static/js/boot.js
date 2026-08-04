window.addEventListener("load", () => {

    const boot = document.getElementById("boot-screen");
    const hud = document.querySelector(".hud");
    const progress = document.getElementById("boot-progress");
    const text = document.getElementById("boot-text");

    hud.style.visibility = "hidden";
    hud.style.opacity = "0";


    let messages = [];
    let i = 0;
    let value = 0;


    fetch("/boot")
    .then(response => response.json())
    .then(data => {

        messages = data.boot.split("\n");


        const timer = setInterval(() => {

            value += 2;

            progress.style.width = value + "%";


            if (value % 20 === 0 && i < messages.length) {

                const message = messages[i++];

                text.textContent = message;


                const speech =
                new SpeechSynthesisUtterance(message);

                speech.rate = 1;
                speech.pitch = 1;

if ('speechSynthesis' in window) {

    speechSynthesis.cancel();

    setTimeout(() => {
        speechSynthesis.speak(speech);
    }, 100);

}
            }


            if (value >= 100) {

                clearInterval(timer);

                boot.style.opacity = "0";


                setTimeout(() => {

                    boot.style.display = "none";

                    hud.style.visibility = "visible";
                    hud.style.opacity = "1";

                },600);

            }


        },40);


    });


});
