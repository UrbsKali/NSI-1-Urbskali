function imc() {
    var t = document.getElementById("taille").value
    var m = document.getElementById("masse").value
    document.getElementById('calc').innerHTML = `Votre IMC est : <i>${10000*m/(t*t)}</i>`
}