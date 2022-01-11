def aumentar(num, aumento = 10, show = False):
    num += num * (aumento / 100)
    if show:
        num = moeda(num)
    return num

def diminuir(num, dimi = 10, show = False):
    num -= num * (dimi / 100)
    if show:
        num = moeda(num)
    return num

def dobro(num, show = False):
    dobro = num * 2
    if show:
        dobro = moeda(dobro)
    return dobro

def metade(num, show = False):
    met = num / 2
    if show:
        met = moeda(met)
    return met

def moeda(num, moeda ='R$'):
    return f'{moeda}{num:>.2f}'.replace('.',',')

def resumo(num, aumento = 10, diminuição = 10):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'{"Preço analisado:":<20}',moeda(num))
    print(f'{"Dobro do preço:":<20}',dobro(num,True))
    print(f'{"Metade do preço:":<20}',metade(num,True))
    print(f'{aumento}{"% de aumento":<18}',aumentar(num,aumento,True))
    print(f'{diminuição}{"% de redução:":<18}',diminuir(num,diminuição,True))
    print('-'*30)