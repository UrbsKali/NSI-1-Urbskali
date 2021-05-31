function IMC(){
    t = document.getElementById("t").value;
    m = document.getElementById("m").value;
    x = 10000 * m / (t * t);
    document.getElementById("calc").innerText = "Votre imc est " + x 
    return x
}

function etat() {
    x = IMC();
    if (x < 18.5) {
        document.getElementById("state").innerText = "Vous êtes en insuffisance pondérale"
    } else if ( 18.5 < x < 25 ){
        document.getElementById("state").innerText = "Vous êtes en poids normal"
    } else if ( 25 <= x < 30 ){
        document.getElementById("state").innerText = "Vous êtes en surpoids"
    } else if ( 30 < x ){
        document.getElementById("state").innerText = "Vous êtes en obésité"
    }
}

function change(){ 
    document.getElementById("big").src= document.getElementById("big").src === `${document.URL}big.png` ? "slim.png" : "big.png"
}

function age(){
    d = new Date()
    year = document.getElementById('an').value
    ans = document.getElementById("ans")
    age_ = d.getFullYear() - parseInt(year)
    if ( age_ < 120){
        ans.innerText = age_
        return age_
    } else {
        alert("Tu t'es trompé sur ton âge")
        return false
    }
}

function getRadioValue() {
    var ele = document.getElementsByName('sexe');
      
    for(i = 0; i < ele.length; i++) {
        if(ele[i].checked)
           return ele[i].value
    }
}

function IMG(){
    img_ = (1,20 * IMC()) + (0,23 * age() ) - (10,8 * parseInt(getRadioValue()) ) - 5,4
    return img_
}