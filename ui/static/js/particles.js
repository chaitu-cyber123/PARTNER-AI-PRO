const field = document.getElementById("particle-field");


if(field){


    for(let i = 0; i < 40; i++){


        const particle = document.createElement("div");


        particle.className = "energy-particle";


        particle.style.left =
        Math.random() * 100 + "%";


        particle.style.animationDuration =
        (5 + Math.random() * 8) + "s";


        particle.style.animationDelay =
        (Math.random() * 8) + "s";


        const size =
        2 + Math.random() * 4;


        particle.style.width =
        size + "px";


        particle.style.height =
        size + "px";


        field.appendChild(particle);


    }


}
