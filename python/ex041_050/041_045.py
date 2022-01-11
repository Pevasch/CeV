# exercício 041
from datetime import datetime

verde = '\033[32m'
limpa = '\033[0m'

ano = datetime.today().year - 4
nasc = int(input(f'Ano de nascimento: {verde}'))
idade = ano - nasc
print(f'{limpa}O atleta tem {idade} anos.')
print('Classificação:',end=' ')
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JÚNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
    
# exercício 042
verde = '\033[32m'
limpa = '\033[0m'

r1 = float(input(f'Primeiro segmento: {verde}'))
r2 = float(input(f'{limpa}Segundo segmento: {verde}'))
r3 = float(input(f'{limpa}Terceiro segmento: {verde}'))
print(f'{limpa}Os segmentos acima',end=' ')
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('PODEM FORMAR um triângulo',end=' ')
    if r1 == r2 and r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('NÃO PODEM formar triângulo.')
    
# exercício 043
verde = '\033[32m'
limpa = '\033[0m'

peso = float(input(f'Qual é o seu peso? (Kg) {verde}'))
altura = float(input(f'{limpa}Qual é sua altura? (m) {verde}'))
imc = peso / (altura**2)
print(f'{limpa}O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.5 < imc < 25:
    print('PARABÉNS, você esta na faixa de PESO NORMAL')
elif 25 < imc < 30:
    print('Sobrepeso')
elif 30 < imc < 40:
    print('Você está em OBESIDADE!')
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
    
# exercício 044
verde = '\033[32m'
limpa = '\033[0m'

print('='*10,' LOJAS GUANABARA ','='*10)
preço = float(input(f'Preço das compras: R${verde}'))
opc = int(input(f'''{limpa}FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/chque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual é a opção? {verde}'''))

if opc == 1:
    print(f'{limpa}Sua compra de R${preço:.2f} vai custar R${preço * 0.9:.2f} no final.')
elif opc == 2:
    print(f'{limpa}Sua compra de R${preço:.2f} vai custar R${preço * 0.95:.2f} no final.')
elif opc == 3:
    print(f'{limpa}Sua compra será parcelada em 2x de R${preço / 2:.2f} SEM JUROS')
    print(f'Sua compra no final sairá pelo mesmo preço de R${preço}')
elif opc == 4:
    parcelas = int(input(f'{limpa}Quantas parcelas? {verde}'))
    print(f'{limpa}Sua compra será parcelada em {parcelas}x de R${(preço * 1.2) / parcelas:.2f} COM JUROS')
    print(f'Sua compra de R${preço:.2f} vai custar R${preço * 1.2:.2f} no final.')
else:
    print('Opção inválida!')
    
# exercício 045
from time import sleep
from random import randint

verde = '\033[32m'
limpa = '\033[0m'

lista = 'Pedra', 'Papel', 'Tesoura'
computador = randint(0,2)
jogador = int(input(f'''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual é a sua jogada? {verde}'''))
sleep(0.2)
print(f'{limpa}JO')
sleep(0.2)
print('KEN')
sleep(0.2)
print('PO!!!')
sleep(0.1)
print('-='*15)
print(f'Computador jogou {lista[computador]}')
print(f'Jogador jogou {lista[jogador]}')
print('-='*15)
if lista[computador] == lista[jogador]:
    print('EMPATE')
elif lista[jogador] == 'Pedra':
    if lista[computador] == 'Papel':
        print('PERDEU!')
    else:
        print('JOGADOR VENCE')
elif lista[jogador] == 'Papel':
    if lista[computador] == 'Pedra':
        print('JOGADOR VENCE')
    else:
        print('PERDEU!')
else:
    if lista[computador] == 'Pedra':
        print('PERDEU!')
    else:
        print('JOGADOR VENCE')
