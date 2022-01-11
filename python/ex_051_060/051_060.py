# exercício 051
verde = '\033[32m'
limpa = '\033[0m'

print('='*30)
print(f'{"10 TERMOS DE UMA PA":^30}')
print('='*30)

p1 = int(input(f'Primeiro termo: {verde}'))
r = int(input(f'{limpa}Razão: {verde}'))
p10 = p1 + (10 - 1) * r
for c in range(p1, p10 + 1,r):
    print(c,end=' -> ')
print('ACABOU')

# exercício 052
verde = '\033[32m'
vermelho = '\033[31m'
amarelo = '\033[93m'
limpa= '\033[0m'

contador = 0
n = int(input(f'Digite um número: {verde}'))
for c in range(1,n+1):
    if n % c == 0:
        cor = amarelo
        contador += 1
    else:
        cor = vermelho
    print(f'{cor}{c}{limpa}',end=' ')
print(f'\nO número {n} foi divisível {contador} vezes')
if contador == 2:
    print('E por isso ele É PRIMO')
else:
    print('E por isso ele NÃO É PRIMO!')

# exercício 053
verde = '\033[32m'
limpa = '\033[0m'

frase = input(f'Digite um frase: {verde}').replace(' ','').upper()
reverso = frase[len(frase)::-1]
print(f'{limpa}O inverso de {frase} é {reverso}')
if reverso == frase:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo')
    
# exercício 054
from datetime import datetime

verde = '\033[32m'
limpa = '\033[0m'

hoje = datetime.today().year - 4
menores, maiores = 0, 0

for c in range(1,8):
    nasc = int(input(f'{limpa}Em que ano a {c}ª pessoa nasceu? {verde}'))
    idade = hoje - nasc
    if idade >= 18:
        maiores += 1
    else:
        menores += 1

print(f'{limpa}Ao todo tivemos {maiores} pessoas maiores de idade')
print(f'E também tivemos {menores} pessoas menores de idade')

# exercício 055
lista = []
verde = '\033[32m'
limpa = '\033[0m'

for c in range(1,6):
    lista.append(input(f'{limpa}Peso da {c}ª pessoa: {verde}'))
print(f'{limpa}O maior peso lido foi de {max(lista)}Kg')
print(f'O menor peso lido foi de {min(lista)}Kg')

# exercício 056
verde = '\033[32m'
limpa = '\033[0m'

média, novinhas, idade_velho,soma, nome_velho = 0,0,0,0,''

for c in range(1,5):
    print(f'{limpa}-'*5,f'{c}ª pessoa','-'*5)
    nome = input(f'{limpa}Nome: {verde}').strip()
    idade = int(input(f'{limpa}Idade: {verde}'))
    sexo = input(f'{limpa}Sexo [M/F]: {verde}').strip()
    soma += idade
    if 'M' in sexo[0].upper():
        if idade_velho == 0 or idade > idade_velho:
            idade_velho = idade
            nome_velho = nome
    elif 'F' in sexo[0].upper() and idade < 20:
        novinhas += 1

média = soma / 4
print(f'{limpa}A média de idade do grupo é de {média:.1f} anos')
print(f'O homem mais velho tem {idade_velho} anos e se chama {nome_velho}.')
print(f'Ao todo são {novinhas} mulheres com menos de 20 anos')

# exercício 057
verde = '\033[32m'
limpa = '\033[0m'

sexo = input(f'Informe seu sexo: [M/F] {verde}').strip().upper()[0]
while 'M' not in sexo and 'F' not in sexo:
    sexo = input(f'{limpa}Dados inválidos. Por favor, informe seu sexo: {verde}').strip().upper()[0]
print(f'{limpa}Sexo {sexo} registrado com sucesso')

# exercício 058
from random import randint

verde = '\033[32m'
limpa = '\033[0m'

escolha = randint(0,10)
palpite = int(input(f'''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?
Qual é seu palpite? {verde}'''))
contador = 1
while escolha != palpite:
    if palpite < escolha:
        print(f'{limpa}Mais...',end=' ')
    else:
        print(f'{limpa}Menos...',end=' ')
    print('Tente mais uma vez')
    palpite = int(input(f'Qual é seu palpite? {verde}'))
    contador += 1
print(f'{limpa}Acertou com {contador} tentativas. Parabéns!')

# exercício 059
verde = '\033[32m'
limpa = '\033[0m'

n1 = int(input(f'Primeiro valor: {verde}'))
n2 = int(input(f'{limpa}Segundo valor: {verde}'))
while True:
    opc = int(input(f'''\t{limpa}[ 1 ] somar
\t[ 2 ] multiplicar
\t[ 3 ] maior
\t[ 4 ] novos números
\t[ 5 ] sair do programa
>>>>> Qual é a sua opção? {verde}'''))
    if opc == 1:
        print(f'{limpa}A soma entre {n1} + {n2} é {n1+n2}')
    elif opc == 2:
        print(f'{limpa}O resultado de {n1} x {n2} é {n1*n2}')
    elif opc == 3:
        print(f'{limpa}entre {n1} e {n2} o maior valor é {max(n1,n2)}')
    elif opc == 4:
        n1 = int(input(f'''{limpa}Informe os números novamente:
Primeiro valor: {verde}'''))
        n2 = int(input(f'{limpa}Segundo valor: {verde}'))
    elif opc == 5:
        print(f'{limpa}Finalizando...')
        break
    else:
        print(f'{limpa}Opção inválida. Tente novamente')
    print(f'{limpa}=-='*10)
print('Fim do programa! Volte Sempre!')

# exercício 060
verde = '\033[32m'
limpa = '\033[0m'

resultado = 1
fatorial = int(input(f'''Digite um número para
calcular seu Fatorial: {verde}'''))
print(f'{limpa}Calculando {fatorial}! =',end=' ')
while not fatorial == 0:
    print(fatorial,end=' ')
    if fatorial != 1:
        print('x',end=' ')
    else:
        print('=', end=' ')
    resultado *= fatorial
    fatorial -= 1
print(resultado)
