function verificar() {
    var date = new Date()
    var hoje = date.getFullYear()
    var res = window.document.querySelector('div#res')
    var fano = window.document.getElementById('txtano')
    
    if (fano.value.length == 0 || Number(fano.value) > hoje) {
        window.alert('[ERRO] Verifique os dados e tente novamente!')
    } else {
        nasc = Number(fano.value)
        var fsex = window.document.getElementsByName('radsex')
        var idade = hoje - nasc
        var genero = ''
        var img = window.document.createElement('img')
        img.setAttribute('id', 'foto')
        res.style.textAlign = 'center'
        if (fsex[0].checked) {
            genero = 'homem'
            if (idade < 10) {
                img.setAttribute('src', 'img_300/boy_300.png')
            } else if (idade < 21) {
                img.setAttribute('src', 'img_300/youngman_300.png')
            } else if (idade < 50) {
                img.setAttribute('src', 'img_300/man_300.png')
            } else {
                img.setAttribute('src', 'img_300/oldman_300.png')
            }
        } else {
            genero = 'mulher'
            if (idade < 10) {
                img.setAttribute('src', 'img_300/girl_300.png')
            } else if (idade < 21) {
                img.setAttribute('src', 'img_300/youngwoman_300.png')
            } else if (idade < 50) {
                img.setAttribute('src', 'img_300/adultwoman_300.png')
            } else {
                img.setAttribute('src', 'img_300/oldwoman_300.png')
            }
        }   
    }
    res.innerHTML = `<p>Detectamos ${genero} com ${idade} anos.</p>`
    res.appendChild(img)
}