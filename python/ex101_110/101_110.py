# exercício 101
def voto():
    from datetime import datetime as dt

    hoje = dt.today().year - 3

    print('-'*20)
    nascimento = int(input('Em que nao você nasceu? '))
    idade = hoje - nascimento

    print(f'Com {idade} anos:',end=' ')

    if idade < 16:
        print('NÃO VOTA.')
    elif idade >= 65 or (idade < 18 and idade > 16):
        print('VOTO OPCIONAL.')
    else:
        print('VOTO OBRIGATÓRIO.')

voto()

# exercício 102
def fatorial(n , show = True):
    print('-' * 20)
    resultado = 1
    for c in range(n, 0, -1):
        resultado *= c
        if show == True:
            print(c,end=' ')
            if c == 1:
                print('=',end=' ')
            else:
                print('x',end=' ')
    return resultado

print(fatorial(5, show = False))

# exercício 103
def ficha(nome = '<desconhecido>', gols = 0):
    if nome == '':
        nome = '<desconhecido>'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')

print('-' * 20)
a = input('Nome do Jogador: ')
b = input('Número de Gols: ')
ficha(a,b)

# exercício 104
def leiaInt(frase):
 print('-'*20)
 r = input(frase)
 while True:
  if r.isnumeric():
   return r
   break
  else:
   print('\33[1;31mERRO! Digite um número inteiro válido.\033[m')
   r = input(frase)


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

# exercício 105
def notas(*notas, sit = False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param notas: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação do aluno
    :return: dicionário com várias informações sobre a situação da turma
    '''
    média = sum(notas) / len(notas)
    boletim = {
        'total' : len(notas),
        'maior' : max(notas),
        'menor' : min(notas),
        'média' : média
    }
    if sit:
        if média < 5:
            situ = 'RUIM'
        elif média >7:
            situ = 'BOA'
        else:
            situ = 'RAZOÁVEL'
        boletim['situação'] = situ
    print('-'*30)
    return boletim

resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)

# exercício 106
def lin(frase):
    tam = len(frase) + 4
    print('~' * tam)
    print(f'  {frase}')
    print('~' * tam)

def corlin(frase, color = 'verde' or 'azul'):
    cores = {
        'verde': '\033[1;42m',
        'azul': '\033[1;44m',
        'branco': '\033[1;107m',
        'vermelho': '\033[1;41m',
        'limpa': '\033[m'
    }
    print(cores[color],end='')
    lin(frase)
    print(cores['limpa'],end ='')

def cor(color = 'limpa'):
    cores = {
        'verde': '\033[1;42m',
        'azul': '\033[1;44m',
        'branco': '\033[1;107m',
        'vermelho': '\033[1;41m',
        'limpa': '\033[m'
    }
    print(cores[color],end='')

while True:
    corlin('SISTEMA DE AJUDA PyHELP','verde')
    resp = input('Função ou Biblioteca > ')
    if resp.upper() == 'FIM':
        break
    corlin(f"Acessando o manual do comando '{resp}'",'azul')
    cor('branco')
    help(resp)
    cor()
corlin('Até logo','vermelho')

# exercício 107
from UtilidadesCeV import moeda as m

valor = float(input('Digite o preço: R$'))
print(f'A metade de R${valor} é R${m.metade(valor)}')
print(f'O dobro de R${valor} é R${m.dobro(valor)}')
print(f'Aumentando 10%, temos R${m.aumentar(valor, 10)}')

# exercício 108
from UtilidadesCeV import moeda as m

valor = float(input('Digite o preço: R$'))
print(f'A metade de {m.moeda(valor)} é {m.moeda(m.metade(valor))}')
print(f'O dobro de {m.moeda(valor)} é {m.moeda(m.dobro(valor))}')
print(f'Aumentando 10%, temos {m.moeda(m.aumentar(valor, 10))}')

# exercício 109
from UtilidadesCeV import moeda as m

valor = float(input('Digite o preço: R$'))
print(f'A metade de {m.moeda(valor)} é {m.metade(valor,show=True)}')
print(f'O dobro de {m.moeda(valor)} é {m.dobro(valor,show=True)}')
print(f'Aumentando 10%, temos {m.aumentar(valor, 10,show=True)}')

# exercício 110
from UtilidadesCeV import moeda as m

valor = float(input('Digite o preço: R$'))
m.resumo(valor,20,12)
