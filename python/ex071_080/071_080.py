# exercício 071
def cor(frase):
    verde = '\033[32m'
    limpa = '\033[0m'

    return f'{limpa}{frase}{verde}'

def caixa(valor):
    ced50,ced20,ced10 = 0,0,0
    while valor != 0:
        if valor / 50 != 0:
            ced50 = int(valor / 50)
            print(cor(f'Total de {ced50} cédulas de R$50'))
            valor -= (50 * ced50)
        if valor / 20 != 0:
            ced20 = int(valor / 20)
            print(cor(f'Total de {ced20} cédulas de R$20'))
            valor -= (20 * ced20)
        if valor / 10 != 0:
            ced10 = int(valor / 10)
            print(cor(f'Total de {ced10} cédulas de R$10'))
            valor -= (10 * ced10)
        if valor / 1 != 0:
            print(cor(f'Total de {valor} cédulas de R$1'))
            valor = 0


print('='*40)
print(f'{"BANCO CEV":^40}')
print('='*40)
saque = int(input(cor('Que valor você quer sacar R$')))
caixa(saque)
print('\033[0m='*40)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')

# exercício 072
def cor(frase):
    verde = '\033[32m'
    limpa = '\033[0m'

    return f'{limpa}{frase}{verde}'

tupla = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze',
         'onze','doze','treze','quatorze','quinze','dezesseis',
         'dezessete','dezoito','dezenove','vinte')

n = int(input(cor('Digite um número entre 0 e 20: ')))
while n > len(tupla)-2 or n < 0:
    n = int(input(cor('Tente novamente. Digite um número entre 0 e 20: ')))
print(cor(f'Você digitou o número {tupla[n]}'))

# exercício 073
brasileirão = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
               'Cruzeiro', 'Flamengo','Vasco','Chapecoense',
               'Atlético - MG', 'Botafogo', 'Atlético - PR',
               'Bahia', 'São Paulo', 'Fluminense', 'Sport',
               'Vitória', 'Coritiba', 'Avaí','Ponte Preta', 'Atlético - GO')

def lin(frase):
    print('-='*40)
    print(frase)

lin(f'Lista de times do Brasileirão: {brasileirão}')
lin(f'Os 5 primeiros são {brasileirão[0:5]}')
lin(f'Os 4 últimos são {brasileirão[:15:-1]}')
lin(f'Times em ordem alfabética: {sorted(brasileirão)}')
lin(f'O Chapecoense está na {brasileirão.index("Chapecoense")+1}ª posição')

# exercício 074
from random import randint

tupla = tuple(randint(0,10) for c in range(5))

print('Os valores sorteados foram: ',*tupla)
print(f'O maior valor sorteado foi {max(tupla)}')
print(f'O menor valor sorteado foi {min(tupla)}')

# exercício 075
def cor(frase):
    verde = '\033[32m'
    limpa = '\033[0m'

    return f'{limpa}{frase}{verde}'

tupla = tuple(int(input(cor(f'Digite o {c}º número: '))) for c in range(1,5))
pares = tuple(c for c in tupla if c % 2 == 0)

print('\033[0mVocê digitou os valores ',tupla)
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
print(f'O valor 3 apareceu na {tupla.index(3)+1}ª posição')
print('Os valores pares digitados foram ',*pares)

# exercício 076
tupla = ('Lápis',1.75,'Borracha',2,'Caderno',15.9,'Estojo',
         25,'Transferidor',4.2,'Compasso',9.99,'Mochila',120.32,
         'Canetas',22.3,'Livro',34.9)

print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for c in range(0,len(tupla),2):
    print(f'{tupla[c]:.<31}R${tupla[c+1]:>7.2f}')
print('-'*40)

# exercício 077
tupla = ('APRENDER','POUCO','FRANGO','PEIXE','CAMINHO','ALEGRIA','LONGE','PYTHON')

for c in tupla:
    print('\n',f'Na palavra {c} temos ',end='')
    for i in c:
        if i.lower() in 'aeiou':
            print(i.lower(),end=' ')

# exercício 078
def cor(frase):
    verde = '\033[32m'
    limpa = '\033[0m'

    return f'{limpa}{frase}{verde}'

lista = [int(input(cor(f'Digite um valor para a Posição {c}: '))) for c in range(0,5)]
print('\033[0m=-'*30)
print(f'Você digitou os valores {lista}')
maior = max(lista)
menor = min(lista)
print(f'O maior valor digitado foi {maior} nas posições',end=' ')
for i in range(len(lista)):
    if maior == lista[i]:
        print(i,end='... ')
print('\n',f'O menor valor digitado foi {menor} nas posições',end=' ')
for i in range(len(lista)):
    if menor == lista[i]:
        print(i,end='... ')
        
# exercício 079
def cor(frase):
    verde = '\033[32m'
    limpa = '\033[0m'

    return f'{limpa}{frase}{verde}'

lista = []
resp = 's'
while resp not in 'Nn':
    n = int(input(cor('Digite um valor: ')))
    if n not in lista:
        lista.append(n)
        print('\033[0mValor adicionado com sucesso...')
    else:
        print('\033[0mValor duplicado! Não vou adicionar...')
    resp = input(cor('Quer continuar [S/N] '))
print('\033[0m-='*30)
print(f'Você digitou os valores {sorted(lista)}')

# exercício 080
def cor(frase):
    verde = '\033[32m'
    limpa = '\033[0m'

    return f'{limpa}{frase}{verde}'

valores = []
for c in range(0,5):
    valor = int(input(cor('Digite um valor: ')))
    if c == 0 or valor > valores[-1]:
        valores.append(valor)
        print('\033[0mAdicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(valores):
            if valor <= valores[pos]:
                valores.insert(pos,valor)
                print(cor(f'Adicionado na posição {pos} da lista...'))
                break
            pos += 1
    '''if c == 0 or max(valores) <= valor:
        valores.append(valor)
        print('\033[0mAdicionado ao final da lista...')
    else:
        for i in range(len(valores)-1,-1,-1):
            if valor <= min(valores):
                valores.insert(0,valor)
                print(cor(f'Adicionado na posição 0 da lista...'))
                break
            elif valor < valores[i] and valor > valores[i-1]:
                valores.insert(i,valor)
                print(cor(f'Adicionado na posição {i} da lista...'))
                break
'''
print('\033[0m-='*30)
print('Os valores digitados em ordem foram',valores)
