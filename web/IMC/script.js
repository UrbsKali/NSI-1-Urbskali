function IMC(){
    t = document.getElementById("t").value;
    m = document.getElementById("m").value;
    x = 10000 * m / (t * t);
    return x
}

function etat() {
    x = IMC();
    tmp = ""
    if (x < 18.5) {
        tmp = "Vous êtes en insuffisance pondérale"
    } else if ( 18.5 < x < 25 ){
        tmp = "Vous êtes en poids normal"
    } else if ( 25 <= x < 30 ){
        tmp = "Vous êtes en surpoids"
    } else if ( 30 < x ){
        tmp = "Vous êtes en obésité"
    }
    return tmp
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
    let img_ = ( 1.20 * IMC() ) + ( 0.23 * age() ) - (10.8 * parseInt(getRadioValue()) ) - 5.4
    return img_
}

function draw_tab(){
    tableau = document.getElementsByClassName("tab-container")[0]
    tableau.innerHTML = `<table class="table text-light">
    <thead>
      <tr>
        <th scope="col">Nom</th>
        <th scope="col">Age</th>
        <th scope="col">IMC</th>
        <th scope="col">IMG</th>
        <th scope="col">Interpretation</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>${document.getElementById("nom").value}</td>
        <td>${age()}</td>
        <td>${Math.round(IMC())}</td>
        <td>${Math.round(IMG())} %</td>
        <td>${etat()}</td>
      </tr>
    </tbody>
  </table>`
}