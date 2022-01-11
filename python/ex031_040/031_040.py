# exercício 031
dist = float(input('Qual é a distância da sua viagem? \033[32m'))
limpa = '\033[0m'
print(f'{limpa}Você está prestes a começar uma viagem de {dist}Km.')
print('E o preço da sua passagem será de R$',end='')
if dist <= 200:
    print(f'{dist*0.5:.2f}')
else:
    print(f'{dist*0.45:.2f}')
   
# exercício 032
from datetime import datetime

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = datetime.today().year
print(f'O ano {ano} é', end=' ')
if ano % 4 == 0 and ano % 100 != 0:
    print('BISSEXTO')
elif ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
    print('BISSEXTO')
else:
    print('NÃO é BISSEXTO')
    
# exercício 033
lista = []
lista.append(input('Primeiro valor: '))
lista.append(input('Segundo valor: '))
lista.append(input('Terceiro valor: '))
print(f'O menor valor digitado foi {min(lista)}')
print(f'O maior valor digitado foi {max(lista)}')

# exercício 034
sal = float(input('Qual é o salário do funcionário? R$\033[32m'))
limpa = '\033[0m'
if sal > 1250: novosal = sal * 1.1
else: novosal = sal * 1.15
print(f'{limpa}Quem ganhava R${sal:.2f} passa a ganhar R${novosal:.2f} agora')

# exercício 035
verde = '\033[32m'
limpa = '\033[0m'
print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
a = float(input(f'Primeiro segmento: {verde}'))
b = float(input(f'{limpa}Segundo segmento: {verde}'))
c = float(input(f'{limpa}Terceiro segmento: {verde}'))
print(f'{limpa}Os segmentos acima',end=' ')
if a + c > b and a + b > c and c + b > a:
    print('PODEM FORMAR',end=' ')
else:
    print('NÃO PODEM FORMAR',end=' ')
print('triângulo!')

# exercício 036
verde = '\033[32m'
limpa = '\033[0m'
val = float(input(f'Valor da casa: R${verde}'))
sal = float(input(f'{limpa}Salário do comprador: R${verde}'))
anos = int(input(f'{limpa}Quantos anos de financiamento? {verde}'))
mensalidade = (val/anos)/12
print(f'{limpa}Para pagar uma casa de R${val:.2f} em {anos} anos a prestação será de R${mensalidade:.2f}')
if mensalidade > sal * 0.3:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo pode ser CONCEDIDO!')
    
# exercício 037
verde = '\033[32m'
limpa = '\033[0m'

n = int(input(f'Digite um número inteiro: {verde}'))
opc = int(input(f'''{limpa}Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL
Sua opção: {verde}'''))
if opc == 1:
    print(bin(n)[2:])
elif opc == 2:
    print(oct(n)[2:])
elif opc == 3:
    print(hex(n)[2:])

# exercício 038
verde = '\033[32m'
limpa = '\033[0m'
n1 = int(input(f'Primeiro número: {verde}'))
n2 = int(input(f'{limpa}Segundo número: {verde}'))
if n1 > n2:
    print(f'{limpa}O PRIMEIRO valor é maior')
elif n2 < n1:
    print(f'{limpa}O SEGUNDO valor é maior')
else:
    print(f'{limpa}Não existe valor maior, os dois são iguais')
    
# exercício 039
from datetime import datetime

verde = '\033[32m'
limpa = '\033[0m'

nasc = int(input(f'Ano de nascimento: {verde}'))
hoje = datetime.today().year - 4
idade = hoje - nasc
print(f'{limpa}Quem nasceu em {nasc} tem {idade} anos em {hoje}.')
if idade < 18:
    print(f'Ainda faltam {18 - idade} anos para o alistamento')
    print(f'Seu alistamento será em {hoje+(18 - idade)}')
elif idade > 18:
    print(f'Você já deveria ter se alistado há {idade - 18} anos')
    print(f'Seu alistamento foi em {hoje - (idade - 18)}')
else:
    print(f'Você tem que se alistar IMEDIATAMENTE!')

# exercício 040
verde = '\033[32m'
limpa = '\033[0m'

n1 = float(input(f'Primeira nota: {verde}'))
n2 = float(input(f'{limpa}Segunda nota: {verde}'))
média = (n1 + n2) / 2
print(f'{limpa}Tirando {n1} e {n2}, a média do aluno é {média:.1f}')
print('O aluno está', end=' ')
if média >= 7:
    print('APROVADO')
elif média < 5:
    print('REPROVADO')
else:
    print('em RECUPERAÇÃO')
