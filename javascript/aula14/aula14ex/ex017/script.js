function tabuada() {
    var caixa = document.querySelector('select#caixa')
    var valor = document.querySelector('input#txtn').value
    var c = 1
    if (valor == '') {
        alert('Por favor, digite um número!')
    } else {
        caixa.innerHTML = ''
        while (c <= 10) {
            caixa.innerHTML += `<option value="opção"> ${valor} x ${c} = ${valor *c}</option>`
            c++    
        }
    }
}