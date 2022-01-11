# exercício 091
print('Valores sorteados:')
jogadores = {
    'jogador1': randint(1,5),
    'jogador2': randint(1,5),
    'jogador3': randint(1,5),
    'jogador4': randint(1,5)
}
jogadores2 = dict()
for k,v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
print('-='*30)
print('  == RANKING DOS JOGADORES ==')
for c in range(0,4):
    for k,v in jogadores.items():
        if v >= sorted(jogadores.values(), reverse=True)[c]:
            jogadores2[k] = v
c = 1
for k, v in jogadores2.items():
    print(f'{c}º lugar: ', end='')
    print(f'{k} com {v}.')
    c += 1
    
# exercício 092
from datetime import datetime as dt

dicio = {
    'nome': input('Nome: '),
    'idade': dt.today().year-3 - int(input('Ano de Nascimento: ')),
    'ctps': int(input('Carteira de Trabalho (0 não tem): '))
}
if dicio['ctps'] != 0:
    dicio['contratação'] = int(input('Ano de Contratação: '))
    dicio['salário'] = float(input('Salário: R$'))
    dicio['aposentadoria'] = (35 - (dt.today().year-3 - dicio['contratação'])) + dicio['idade']
print('-='*30)
for k,v in dicio.items():
    print(f'\t-{k} tem o valor {v}')
    
# exercício 093
gols = []
geral = {
    'nome': input('Nome do Jogador: ')
}
partidas = int(input(f'Quantas partidas {geral["nome"]} jogou? '))
for c in range(partidas):
    gols.append(int(input(f'    Quantos gols na partida {c}? ')))
geral['gols'] = gols
geral['total'] = sum(gols)
print('-='*30)
print(geral)
print('-='*30)
for k,v in geral.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {geral["nome"]} jogou {partidas} partidas.')
for i,v in enumerate(gols):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {geral["total"]} gols.')

# exercício 094
cadastro = {}
geral = []
medidade = 0
mulheres = []
resp = 'S'
while resp in 'Ss':
    cadastro['nome'] = input('Nome: ').strip()
    while True:
        cadastro['sexo'] = input('Sexo: [M/F] ').strip().upper()[0]
        if cadastro['sexo'] in 'MmFf':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    if cadastro['sexo'] in 'Ff':
        mulheres.append(cadastro['nome'])
    cadastro['idade'] = float(input('Idade: '))
    medidade += cadastro['idade']
    while True:
        resp = input('Quer continuar? [S/N] ').strip().upper()[0]
        if resp in 'NnSs':
            break
        print('ERRO! Responda apenas S ou N.')
    geral.append(cadastro.copy())
print('-='*30)
medidade = medidade/len(geral)
print(f'A) Ao todo temos {len(geral)} pessoas cadastradas.')
print(f'B) A média de idade é de {medidade:.2f} anos.')
print('C) As mulheres cadastradas foram', *mulheres)
print('D) Lista das pessoas que estão acima da média:')
for n in geral:
    if n['idade'] > medidade:
        print('\t',end='')
        for k,v in n.items():
            print(f'{k} = {v};',end=' ')
        print('\n',end='')
print('<< ENCERRADO >>')

# exercício 095
gols, time = [], []
geral = {}
while True:
    geral['nome'] = input('Nome do Jogador: ').strip()
    partidas = int(input(f'Quantas partidas {geral["nome"]} jogou? '))
    for c in range(partidas):
        gols.append(int(input(f'    Quantos gols na partida {c+1}? ')))
    geral['gols'] = gols.copy()
    geral['total'] = sum(gols)
    gols.clear()
    resp = input('Quer continuar? [S/N] ').strip()[0].upper()
    time.append(geral.copy())
    if resp in 'N':
        break
print('-='*30)
print(f'cod {"nome":<10}{"gols":<10}total')
print('-'*30)
for p in range(len(time)):
    print(p,end=' ')
    for v in time[p].values():
        print(f'{v}', end=' ')
    print('\n',end='')
while True:
    print('-' * 30)
    resp = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if resp == 999:
        break
    elif resp >= len(time):
        print(f'ERRO! Não existe jogador com código {resp}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[resp]["nome"]}:')
        for c in range(len(time[resp]["gols"])):
            print(f'\tNo jogo {c+1} fez {time[resp]["gols"][c]}')
print('<< VOLTE SEMPRE >>')

# exercício 096
def área(l,c):
    area = l * c
    print(f'A área de um terreno {l}x{c} é de {area}m².')

print(' Controle de Terrenos')
print('-'*25)
a = float(input('LARGURA (m): '))
b = float(input('COMPRIMENTO (m): '))
área(a,b)

# exercício 097
def escreva(a):
    tamanho = len(a) +2
    print('~' * tamanho)
    print(f' {a}')
    print('~' * tamanho)

escreva('Gustavo Guanabara')

escreva('Lararara')

# exercício 098
def contador(a,b,c):
    print('-=' * 20)
    print(f'Contagem de {a} até {b} de {c} em {c}')
    if a > b and c > 0:
        c = -c
    if a < b and c < 0:
        c = -c

    for cont in range(a,b+c,c):
        if cont >=  b:
            print(cont,end=' ')
        elif a < b:
            print(cont,end=' ')
    print('FIM!')

contador(1,10,1)
contador(10,0,2)

print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

contador(i,f,p)

# exercício 099
def maior(*a):
    print('-='*30)
    print('Analisando os valores passados...')
    print(*a,f'Foram informados {len(a)} valores ao todo.')
    if len(a) == 0:
        print(f'O maior valor informado foi 0.')
    else:
        print(f'O maior valor informado foi {max(a)}.')

maior(4,7,2,87,2,7,7,7,6,4,89,4,4)

# exercício 100
def sorteia():
    from random import randint
    n = [randint(1,10) for i in range(5)]
    return n

def somaPar(valores):
    soma = 0
    for n in valores:
        if n % 2 == 0:
            soma += n
    return soma


números = sorteia()
print('Sorteando 5 valores da lista:',*números,'PRONTO!')
print('Somando os valores pares de',números,f', temos {somaPar(números)}')
