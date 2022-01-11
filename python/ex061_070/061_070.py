# exercício 061
verde = '\033[32m'
limpa = '\033[0m'

print('Gerador de PA')
print('-='*10)
p1 = int(input(f'Primeiro termo: {verde}'))
r = int(input(f'{limpa}Razão da PA: {verde}'))
p10 = p1 + (10 - 1) * r
while p1 != p10+r:
    print(p1,end=' -> ')
    p1 += r
print('FIM')

# exercício 062
from time import sleep

verde = '\033[32m'
amarelo = '\033[93m'
limpa = '\033[0m'
contador = 0


print('Gerador de PA')
print('-='*10)
p1 = int(input(f'Primeiro termo: {verde}'))
r = int(input(f'{limpa}Razão da PA: {verde}'))
p10 = p1 + (10 - 1) * r
while p1 != p10+r:
    print(f'{amarelo}{p1}',end=' -> ')
    contador += 1
    p1 += r
print('PAUSA')
pY = p10
while True:
    ver = int(input(f'{limpa}Quantos termos você quer mostrar a mais? {verde}'))
    pX = pY + (ver - 1) * r
    if ver == 0:
        break
    else:
        while pY != pX+r:
            print(f'{amarelo}{pY}',end=' -> ')
            contador += 1
            pY += r
            sleep(0.3)
        pY = pX
        print('PAUSA')
print(f'{limpa}Progressão finalizada com {contador} termos mostrados')

# exercício 063
verde = '\033[32m'
limpa = '\033[0m'
a,b = 0,1
contador = 2

print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
termos = int(input(f'Quantos termos você quer mostrar? {verde}'))
print(f'{limpa}~'*30)
print(f'{a} -> {b} -> ',end='')
while contador != termos:
    contador += 1
    c = a + b
    a,b = b,c
    print(c,end=' -> ')
print('FIM')
print('~'*30)

# exercício 064
verde = '\033[32m'
limpar = '\033[0m'
contador, soma = 0,0

while True:
    n = int(input(f'{limpar}Digite um número [999 para parar]: {verde}'))
    if n == 999:
        break
    contador += 1
    soma += n
print(f'{limpar}Você digitou {contador} números e a soma entre eles foi {soma}.')

# exercício 065
verde = '\033[32m'
limpar = '\033[0m'
contador, média, maior, menor, soma = 0,0,0,0,0

while True:
    n = int(input(f'{limpar}Digite um número: {verde}'))
    contador += 1
    soma += n
    if contador == 1:
        maior,menor = n, n
    if maior < n:
        maior = n
    if menor > n:
        menor = n
    resp = input(f'{limpar}Quer continuar?[S/N] {verde}').strip()[0].upper()
    if 'N' in resp:
        break
média = soma / contador
print(f'{limpar}Você digitou {contador} números e a média foi {média:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')

# exercício 066
contador,soma = 0,0

while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    contador += 1
    soma += n
print(f'A soma dos {contador} valores foi {soma}!')

# exercício 067
verde = '\033[32m'
limpar = '\033[0m'

while True:
    n = int(input(f'{limpar}Quer ver a tabuada de qual valor? {verde}'))
    if n <= -1:
        break
    print(f'{limpar}-'*30)
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
    print('-'*30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')

# exercício 068
from random import randint

verde = '\033[32m'
limpar = '\033[0m'
contador,soma, resultado = 0,0,str

print('-='*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
while True:
    print('-='*20)
    jogador = int(input(f'{limpar}Diga um valor: {verde}'))
    parimpar = input(f'{limpar}Par ou Ímpar? [P/I] {verde}').strip().upper()[0]
    computador = randint(0,9)
    soma = jogador + computador
    print(f'{limpar}-'*40)
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {soma}', end=' ')
    if soma % 2 == 0:
        print('DEU PAR')
        resultado = 'P'
    else:
        print('DEU ÍMPAR')
        resultado = 'I'
    print('-'*40)
    if resultado == parimpar:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        contador += 1
    else:
        break

print('Você PERDEU!')
print('-='*20)
print(f'GAME OVER! Você venceu {contador} vezes.')

# exercício 069
verde = '\033[32m'
limpar = '\033[0m'
m18, macho, novinhas = 0,0,0

while True:
    print(f'{limpar}-'*40)
    print(f'{"CADASTRE UMA PESSOA":^40}')
    print('-'*40)
    idade = int(input(f'Idade: {verde}'))
    sexo = input(f'{limpar}Sexo: [M/F] {verde}').strip().upper()[0]
    print(f'{limpar}-'*40)
    if idade > 18:
        m18 += 1
    if sexo == 'M':
        macho += 1
    if idade < 20 and sexo == 'F':
        novinhas += 1
    continuar = input(f'Quer continuar? [S/N] {verde}').strip().upper()[0]
    if continuar == 'N':
        break
print(f'{limpar}Total de pessoas com mais de 18 anos: {m18}')
print(f'Ao todo temos {macho} homem cadastrados')
print(f'E temos {novinhas} mulheres com menos de 20 anos')

# exercício 070
verde = '\033[32m'
limpar = '\033[0m'
total,p1000,p_barato,p_barato_preço,contador = 0,0,str,float,0

print('-'*40)
print(f'{"LOJA SUPER BARATÃO":^40}')
print('-'*40)
while True:
    nome = input(f'{limpar}Nome do Produto: {verde}').strip()
    preço = float(input(f'{limpar}Preço: R${verde}'))
    total += preço
    contador += 1
    if preço > 1000:
        p1000 += 1
    if contador == 1:
        p_barato = nome
        p_barato_preço = preço
    elif p_barato_preço > preço:
        p_barato = nome
        p_barato_preço = preço
    resp = input(f'{limpar}Quer continuar? [S/N] {verde}').strip().upper()[0]
    if resp == 'N':
        break
print(f'{limpar}-'*10,' FIM DO PROGRAMA ','-'*10)
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {p1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {p_barato} que custa R${p_barato_preço:.2f}')
