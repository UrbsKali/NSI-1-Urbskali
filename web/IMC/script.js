function IMC(){
    t = document.getElementById("t").value;
    m = document.getElementById("m").value;
    x = 10000 * m / (t * t);
    document.getElementById("calc").innerText = "Votre imc est " + x ;
    return x
}

function etat() {
    x = IMC();
    if (x < 18.5) {
        document.getElementById("state").innerText = "Vous êtes en insuffisance pondérale";
    } else if ( 18.5 < x < 25 ){
        document.getElementById("state").innerText = "Vous êtes en poids normal";
    } else if ( 25 <= x < 30 ){
        document.getElementById("state").innerText = "Vous êtes en surpoids";
    } else if ( 30 < x ){
        document.getElementById("state").innerText = "Vous êtes en obésité";
    }
}

function change(){ 
    document.getElementById("big").src= document.getElementById("big").src === `${document.URL}big.png` ? "slim.png" : "big.png"
}
   