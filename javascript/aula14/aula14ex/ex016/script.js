
function contar() {
    var i = document.querySelector('input#i').value
    var f = document.getElementById('f').value
    var p = document.getElementById('p').value
    var seta = String.fromCodePoint(0x1F449)
    var fim = String.fromCodePoint(0x1F3F4)
    //var leão = '&#x1F981'
    var res = document.getElementById('res')
    if (i == '' || f == '' || p == '') {
        res.innerHTML = 'Impossível contar!'
    } else {
        if (p < 1) {
            alert('Passo inválido. Considerando PASSO 1!')
            p = 1
        }
        i = Number(i)
        f = Number(f)
        p = Number(p)
        res.innerHTML = 'Contando:<br>'
        if (i > f) {
            for (var c = i; c >= f; c -= p){
                res.innerHTML += c + seta
            }
        }else {
            for (var c = i; c <= f; c += p){
                res.innerHTML += c + seta
            }
        }
        res.innerHTML += fim
    }
}