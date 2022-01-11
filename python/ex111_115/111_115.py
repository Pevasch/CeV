# exercício 112
from UtilidadesCeV.dado import leiaDinheiro
from UtilidadesCeV import moeda as m

money = leiaDinheiro('Digite o preço: R$')
m.resumo(money, 35, 22)

# exercício 113
def leiaInt(frase):
 while True:
  try:
   r = int(input(frase))
  except KeyboardInterrupt:
   print('\33[1;31mUsuário preferiu não digitar esse número.\033[m')
   return 0
  except:
   print('\33[1;31mERRO! Digite um número inteiro válido.\033[m')
  else:
   return r


def leiaFloat(frase):
 while True:
  try:
   r = float(input(frase))
  except KeyboardInterrupt:
   r = 0
   print('\33[1;31mUsuário preferiu não digitar esse número.\33[m')
  except:
   print('\33[1;31mERRO! Digite um número real válido.\033[m')
  else:
   return r

i = leiaInt('Digite um Inteiro: ')
f = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {i} e o real foi {f}')

# exercício 114
import requests as r

# pode usar import urllib.request

try:
    r.get('http://pudim.com.br/').status_code
except:
    print('\33[1;31mO site Pudim não está acessível no momento.\33[m')
else:
    print('\33[1;32mConsegui acessar o site Pudim com sucesso!\33[m')
    
# exercício 115
from UtilidadesCeV.sistema import *

testeCadastrado()
menu()
