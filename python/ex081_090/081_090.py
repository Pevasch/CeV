# exercício 081
def cor(f):
    v = '\033[32m'
    l = '\033[0m'

    return f'{l}{f}{v}'

lista,cont,resp = [],0,'s'
while resp not in 'Nn':
    n = int(input(cor('Digite um valor: ')))
    lista.append(n)
    cont += 1
    resp = input(cor('Quer continuar? [S/N] ')).strip()[0]
print('\033[0m-='*30)
print(f'Você digitou {cont} elementos.')
print(f'Os valores em ordem decrescente são {sorted(lista)[::-1]}')
if lista.index(5):
    print('O valor 5 faz parte da lista!')
    
# exercício 082
def cor(f):
    v = '\033[32m'
    l = '\033[0m'

    return f'{l}{f}{v}'

lista,pares,ímpares,resp = [],[],[],'s'
while resp not in 'Nn':
    n = int(input(cor('Digite um valor: ')))
    lista.append(n)
    resp = input(cor('Quer continuar? [S/N] ')).strip()[0]
print('\033[0m-='*30)
for valor in lista:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        ímpares.append(valor)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')

# exercício 083
def cor(f):
    v = '\033[32m'
    l = '\033[0m'

    return f'{l}{f}{v}'

errado = 0
n = input(cor('Digite a expressão: ')).strip()
abriu = []
fechou = []
if n.count('(') == n.count(')'):
    for p, v in enumerate(n):
        if v == '(':
            abriu.append(p)
        if v == ')':
            fechou.append(p)

    for p, v in enumerate(abriu):
        if v > fechou[p]:
            errado += 1

if n.count('(') == n.count(')') and errado == 0:
    print(cor('Sua expressão está válida!'))
else:
    print(cor('Sua expressão está errada!'))


'''n = input(cor('Digite a expressão: ')).strip()
pilha = []
for símb in n:
    if símb == '(':
        pilha.append('(')
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()
            print(1)
        else:
            pilha.append(')')
            print(2)
            break
if len(pilha) == 0:
    print('Sua espressão está válida!')
else:
    print('Sua expressão está errada!')'''

# exercício 084
contador = 0
peso = 0
maior, menor = 0, 0
lista = []

while True:
    nome = input('Nome: ').strip()
    peso = float(input('Peso: '))
    lista.append(nome)
    lista.append(peso)
    if contador == 0:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
    resp = input('Quer continuar? [S/N] ').strip()[0]
    contador += 1
    if resp in 'Nn':
        break
print('-='*40)
print(f'Ao todo, você cadastrou {contador} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ',end='')
for i in range(len(lista)):
    if lista[i] == maior:
        print(f'[{lista[i-1]}]',end=' ')
print(f'\nO menor peso foi de {menor}Kg. Peso de ',end='')
for i in range(len(lista)):
    if lista[i] == menor:
        print(f'[{lista[i-1]}]',end=' ')

# exercício 085
pares,ímpares = [],[]
lista = [pares,ímpares]

for c in range (1,8):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        ímpares.append(n)

print('-='*30)
print(f'Os valores pares digitados foram : {sorted(lista[0])}')
print(f'Os valores ímpares digitados foram: {sorted(lista[1])}')

# exercício 086
n = []

for c in range(3):
    for p in range(3):
     n.append(input(f'Digite um valor para [{c}, {p}]: '))
print('-='*30)
for c in range(0,7,3):
    for p in range(3):
        print(f'[ {n[c+p]:^3} ]',end='')
    print()
    
# exercício 087
matriz = [[0,0,0],[0,0,0],[0,0,0]]
pares, terceirac, segundal = 0, 0, 0
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        terceirac += matriz[l][2]
        if segundal == 0 or segundal < matriz[1][c]:
            segundal = matriz[1][c]
print('-='*30)
for l in range(3):
    for c in range(3):
        print(f'[ {matriz[l][c]:^3} ]',end='')
    print()
print('-='*30)
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {terceirac}.')
print(f'O maior valor da segunda linha é {segundal}.')

# exercício 088
from random import randint

jogo = []
sorteado = 0

print('-'*30)
print(f'{"JOGO NA MEGA SENA":^30}')
print('-'*30)
n = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-= SORTEANDO {n} JOGOS -=-=-=')
for c in range(1,n+1):
    print(f'Jogo {c}: ',end='')
    for p in range(6):
        sorteado = randint(1, 60)
        while sorteado in jogo:
            sorteado = randint(1,60)
        jogo.append(sorteado)
    print(sorted(jogo))
    jogo.clear()
print('-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=')

# exercício 089
alunos, notas, geral = [], [], []

while True:
    alunos.append(input('Nome: ').strip())
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    alunos.append(notas[:])
    resp = input('Quer continuar? [S/N] ').strip()[0].upper()
    geral.append(alunos[:])
    notas.clear()
    alunos.clear()
    if resp in 'N':
        break
print('-='*30)
print(f'{"Nº":3}{"NOME":15}{"MÉDIA":10}')
print('-'*30)
for i, v in enumerate(geral):
    print(f'{i:<3}{v[0]:15}{(v[1][0] + v[1][1]) / 2:<10}')
print('-'*40)
while True:
    n = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if n == 999:
        break
    print(f'Notas de {geral[n][0]} são {geral[n][1]}')
    print('-'*40)
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')

# exercício 090
boletim = {}

boletim['nome'] = input('Nome: ').strip()
boletim['média'] = float(input(f'Média de {boletim["nome"]}: '))
if boletim['média'] >= 7:
    boletim['situação'] = 'Aprovado'
elif boletim['média'] <= 5:
    boletim['situação'] = 'Reprovado'
else:
    boletim['situação'] = 'Recuperação'
print('-='*30)
for k, v in boletim.items():
    print(f' - {k} é igual a {v}')
    
