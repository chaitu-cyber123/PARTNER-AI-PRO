const orbElement = document.getElementById("orb");

const micButton = document.getElementById("mic-btn");

const statusText = document.getElementById("status-text");



let listening = false;



if(micButton){


   micButton.addEventListener("click",()=>{

orb.className="orb";

listening=!listening;

if(listening){

orb.classList.add("listening");

statusText.innerHTML="LISTENING";

}
else{

orb.classList.add("idle");

statusText.innerHTML="READY";

}

});
      
function updateClock(){

    const now = new Date();

    const time = now.toLocaleTimeString();

    const c1 = document.getElementById("clock");
    const c2 = document.getElementById("clock2");

    if(c1) c1.innerHTML = time;
    if(c2) c2.innerHTML = time;
}

setInterval(updateClock,1000);

updateClock();
}
setInterval(()=>{

    const cpu = document.getElementById("cpu");
    const ram = document.getElementById("ram");

    if(cpu)
        cpu.innerHTML = Math.floor(Math.random()*35+15)+"%";

    if(ram)
        ram.innerHTML = Math.floor(Math.random()*40+30)+"%";

},1200);
