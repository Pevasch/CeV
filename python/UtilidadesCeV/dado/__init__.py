def leiaDinheiro(frase):
    while True:
        din = input(frase)

        din = din.replace(',','.')
        din2 = din.replace('.','')
        if not din2.isnumeric():
            print(f'ERRO! \"{din}\" é um preço inválido!')
        else:
            break
    return float(din)