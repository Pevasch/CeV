while True:
    print('Hello, these are the exercises 001 to 010!')
    resp = int(input('Type "0" to end the program or type the number of the exercise you want to see: '))
    print('')

    if resp == 0:
        break
    elif resp == 1:
        # exercício 001
        print('Olá, Mundo!')
    elif resp == 2:
        # exercício 002
        nome = input('Qual o seu nome? ').strip()
        print('É um prazer te conhecer, ',nome,'!')
    elif resp == 3:
        # exercício 003
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
    
        print(f'A soma entre {n1} e {n2} é igual {n1+n2}!')
    elif resp == 4:
        # exercício 004
        word = input('Digite algo: ').strip()
        print(f'O tipo primitivo desse valor é {type(word)}')
        print(f'Só tem espaços? {word.isspace()}')
        print(f'É um número? {word.isnumeric()}')
        print(f'É alfabético? {word.isalnum()}')
        print(f'Está em maiúsculas? {word.isupper()}')
        print(f'Está em minúsculas? {word.islower()}')
        print(f'Está capitalizado? {word.istitle()}')
    elif resp == 5:
        # exercício 005
        n = int(input('Digite um número: '))
        print(f'Analisando o valor {n}, seu antecessor é {n-1} e o sucessor é {n+1}')
    elif resp == 6:
        # exercício 006
        n = int(input('Digite um número: '))
        print(f'O dobro de {n} vale {n*2}.')
        print(f'O triplo de {n} vale {n*3}.')
        print(f'A raiz quadrada de {n} é igual a {n**(1/2):.2f}.')
    elif resp == 7:
        # exercício 007
        n1 = float(input('Primeira nota do aluno: '))
        n2 = float(input('Segunda nota do aluno: '))
        print(f'A média entre {n1} e {n2} é igual a {(n1+n2)/2:.1f}')
    elif resp == 8:
        # exercício 008
        m = float(input('Uma distância em metros: '))
        print(f'A medida de {m}m corresponde a')
        print(f'{m/1000}km')
        print(f'{m/100}hm')
        print(f'{m/10}dam')
        print(f'{m*10}dm')
        print(f'{m*100}cm')
        print(f'{m*1000}mm')
    elif resp == 9:
        # exercício 009
        n = int(input('Digite um número para ver sua tabuada: '))
        print('-'*10)
        for c in range(1,11):
            print(f'{n} x {c} = {n*c}')
        print('-'*10)
    elif resp == 10:
        # exercício 010
        real = float(input('Quanto dinheiro você tem na carteira? R$'))
        print(f'Com R${real} você pode comprar U${real/3.27:.2f}')
    else:
        print('Sorry, the number that you wrote doesn\'t have a exercise associated with it.')
    print('')