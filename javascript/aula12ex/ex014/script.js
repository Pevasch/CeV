function carregar() {
    var msg = window.document.getElementById('msg')
    var foto = window.document.getElementById('imagem')
    var data = new Date()
    //var hora = data.getHours()
    hora = 12
    msg.innerHTML = `Agora são ${hora} horas.`
    if (hora >= 0 && hora < 12) {
        // Bom dia
        foto.src = 'imagens/manha_300.png'
        window.document.body.style.background = '#b78555'
    } else if (hora >= 12 && hora < 18) {
        // boa tarde
        foto.src = 'imagens/tarde_300.png'
        window.document.body.style.background = '#f8a054'
    } else {
        // boa noite
        foto.src = 'imagens/noite_300.png'
        window.document.body.style.background = '#0a282c'
    }
}
