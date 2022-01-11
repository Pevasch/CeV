# exercício 011
larg = float(input('Largura da parede: '))
altu = float(input('Altura da parede: '))
area = larg * altu
print(f'Sua parede tem a dimensão de {larg}x{altu} e sua área é de {area}m².')
print(f'Para pintar essa parede, você precisará de {area/2}l de tinta.')

# exercício 012
preço = float(input('Qual é o preço do produto? R$'))
print(f'O produto que custava R${preço}, na promoção com desconto de 5% vai custar R${preço*0.95}:.2f')

# exercício 013
sal = float(input('Qual é o salário do Funcionário? R$'))
print(f'Um funcionário que ganhava R${sal}, com 15% de aumento, passa a receber R${sal*1.15:.2f}')

# exercício 014
celsius = float(input('Informe a temperatura em ºC: '))
print(f'A temperatura de {celsius}ºC corresponde a {(celsius*9/5)+32}ºF!')

# exercício 015
dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos Km rodados? '))
print(f'O total a pagar é de R${(dias*60)+(km*0.15):.2f}')

# exercício 016
n = float(input('Digite um valor: '))
print(f'O valor digitado foi {n} e a sua porção inteira é {n//1:.0f}')
print(int(n))

# exercício 017
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
print(f'A hipotenusa vai medir {((co**2)+(ca**2))**(1/2):.2f}')

# exercício 018
from math import radians,sin,cos,tan

ang = float(input('Digite o ângulo que você deseja: '))
rad = radians(ang)
print(f'O ângulo de {ang} tem o SENO de {sin(rad):.2f}')
print(f'O ângulrado de {ang} tem o COSSENO de {cos(rad):.2f}')
print(f'O ângulo de {ang} tem a TANGENTE de {tan(rad):.2f}')

# exercício 019
from random import choice

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
alunos = [n1,n2,n3,n4]
print('O aluno escolhido foi',choice(alunos))

# exercício 020
from random import shuffle

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
alunos = [n1, n2, n3, n4]
shuffle(alunos)
print('A ordem de apresentação será')
print(alunos)
