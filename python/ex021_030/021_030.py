# exercício 021
import pygame

pygame.init()
pygame.mixer.music.load('C:\\Users\\chpev\\Downloads\\Castamere.mp3')
pygame.mixer.music.play()
input()

# exercício 022
nome = input('Digire seu nome completo: ').strip()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras')
if nome.find(" ") == -1:
    print(f'Seu primeiro nome é {nome[0:len(nome)]}')
else:
    print(f'Seu primeiro nome é {nome[0:nome.find(" ")]}')

# exercício 023
n = int(input('Informe um número: '))
print('Analisando o número',n)
if n % 10 != 0:
    print(f'Unidade: {n%10}')
if n % 100 != 0:
    print(f'Dezena: {(n % 100) // 10}')
if n % 1000 != 0:
    print(f'Centena: {(n % 1000) // 100}')
if n % 10000 != 0:
    print(f'Milhar: {(n % 10000) // 1000}')

# exercício 024
cidade = input('Em que cidade você nasceu? ').strip()
print('SANTO' in cidade.upper())

# exercício 025
nome = input('Qual é seu nome completo? ').strip()
print('Seu nome tem Silva?', 'silva' in nome.lower())

# exercício 026
frase = input('Digite uma frase: ').strip().lower()
print(f'A letra A aparece {frase.count("a")} vezes na frase.')
print(f'A primeira letra A apareceu na posição {frase.find("a") + 1}')
print(f'A última letra A apareceu na posição {frase.rfind("a") + 1}')

# exercício 027
nome = input('Digite seu nome completo: ').strip()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {nome[0:nome.find(" ")]}')
print(f'Seu último nome é {nome[nome.rfind(" "):]}')

# exercício 028
from random import randint
from time import sleep

def cor(cores, frase=str):
    fim = '\033[0m'
    if cores == 'branco':
        return f'\033[0m{frase}{fim}'
    if cores == 'amarelo':
        return f'\033[93m{frase}{fim}'
    if cores == 'azul':
        return f'\033[34m{frase}{fim}'
    if cores == 'vermelho':
        return f'\033[31m{frase}{fim}'
    if cores == 'lilás':
        return f'\033[35m{frase}{fim}'
    if cores == 'verde':
        return f'\033[32m{frase}{fim}'

verde = '\033[32m'
print(cor('amarelo','-='*30))
print(cor('azul', 'Vou pensar em um número entre 0 e 5. Tente advinhar...'))
print(cor('amarelo','-='*30))
jog = int(input(f'Em que número eu pensei? {verde}'))
'\033[0m'
print(cor('lilás','Processando'),end='')
for c in range(0,3):
    sleep(0.3)
    print(cor('lilás','.'),end='')
computador = randint(0,5)
print('')
if computador != jog:
    print(cor('vermelho', f'GANHEI! Eu pensei no número {computador} e não no {jog}!'))
else:
    print(cor('amarelo','PARABÉNS! Você conseguiu me vencer!'))
  
# exercício 029
verde = '\033[32m'
amarelo = '\033[93m'
vermelho = '\033[31m'
vel = int(input(f'Qual é a velocidade atual do carro? {verde}'))
if vel > 80:
    multa = (vel - 80) * 7
    print(f'{vermelho}MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print(f'Você deve pagar uma multa de {amarelo}R${multa:.2f}!')
print(f'{amarelo}Tenha um bom dia! Dirija com segurança!')

# exercício 030
lilás = '\033[35m'
azul = '\033[34m'
verde = '\033[32m'
fim = '\033[0m'
n = int(input(f'{lilás}Me diga um número qualquer: {verde}'))
print(f'{fim}O número {n} é{azul}',end=' ')
if n % 2 != 0:
    print('ÍMPAR')
else:
    print('PAR')

