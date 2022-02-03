let lary = []

function adicionar() {
    res.innerHTML = ''
    let caixa= document.querySelector('select#caixa')
    let nm = document.querySelector('input#txtn')
    let num = Number(nm.value)
    if (lary.indexOf(num) != -1 || num < 1 || num > 100 || num == '') {
        alert('Valor inválido ou já encontrado na lista.')
    } else {
        lary.push(num)
        caixa.innerHTML +=  `<option value="opção">Valor ${num} foi adicionado</option>`
    }
    nm.value = ''
    nm.focus()
}

function finalizar() {
    let res = document.querySelector('div#res')
    if (lary.length == 0) {
        alert('Adicione valores antes de finalizar!')
    } else {
        let maior = lary[0]
        let menor = lary[0]
        let soma = 0

        for (c = 0; c < lary.length; c++) {
            if (maior < lary[c]) {
                maior = lary[c]
            }
            if (menor > lary[c]) {
                menor = lary[c]
            }
            soma += lary[c]
        }
        
        res.innerHTML += `<p>Ao todo temos ${lary.length} números cadastrados.</p>`
        res.innerHTML += `<p>O maior valor informado foi ${maior}.</
        p>`
        res.innerHTML += `<p>O menor valor informado foi ${menor}.</
        p>`
        res.innerHTML += `<p>Somando todos os valores, temos ${soma}.</p>`
        res.innerHTML += `<p>A média dos valores digitados é ${soma/lary.length}.</p>`
    }
}
