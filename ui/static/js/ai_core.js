const orb = document.getElementById("orb");

let angle = 0;

function animateCore() {

    angle += 0.02;

    const scale = 1 + Math.sin(angle) * 0.08;

    orb.style.transform =
        `scale(${scale})`;

    requestAnimationFrame(animateCore);

}

animateCore();


// Floating glow

setInterval(function(){

    const glow =
        60 + Math.random()*30;

    orb.style.boxShadow =
        `0 0 20px cyan,
         0 0 ${glow}px cyan,
         0 0 ${glow+40}px cyan`;

},400);


// Idle particles

for(let i=0;i<25;i++){

    const p=document.createElement("div");

    p.className="particle";

    p.style.left=Math.random()*100+"vw";

    p.style.top=Math.random()*100+"vh";

    p.style.animationDuration=
        (5+Math.random()*8)+"s";

    document.body.appendChild(p);

}
