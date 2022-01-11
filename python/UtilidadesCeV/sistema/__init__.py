def menu():
    print('-'*40)
    print('MENU PRINCIPAL'.center(40))
    print('-'*40)
    print('\33[1;33m1\33[m - \33[1;34mVer pessoas cadastradas\33[m')
    print('\33[1;33m2\33[m - \33[1;34mCadastrar nova Pessoa\33[m')
    print('\33[1;33m3\33[m - \33[1;34mSair do Sistema\33[m')
    print('-'*40)
    opc()


def opc():
    op = int(input('\33[1;33mSua Opção: \33[m'))

    if op == 1:
        arquivo =open('Nomes','r')
        for linha in arquivo:
            print(linha,end='')
        arquivo.close()
        menu()
    elif op == 2:
        arquivo = open('Nomes', 'r')
        nome = input('Nome: ')
        try:
            idade = int(input('Idade: '))
        except:
            print('\33[1;31mERRO: por favor, digite um número inteiro válido.\33[m')
            idade = int(input('Idade: '))
        conteudo = arquivo.readlines()
        conteudo.append(f'{nome:<30}')
        conteudo.append(str(idade) +' anos' + '\n')
        arquivo.close()

        arquivo = open('Nomes' , 'w')
        arquivo.writelines(conteudo)
        arquivo.close()

        print(f'Novo registro de {nome} adicionado.')
        menu()
    elif op == 3:
        print('-' * 40)
        print('Saindo do sistema... Até logo!'.center(40))
        print('-' * 40)
    else:
        print('\33[1;31mERRO! Digite uma opção válida!\33[m')
        menu()


def testeCadastrado():
    arquivo = open('Nomes','r')
    if arquivo.read() == '':
        escrever = open('Nomes','w')
        escrever.write('-'*40+'\n')
        escrever.write('PESSOAS CADASTRADAS'.center(40)+'\n')
        escrever.write('-'*40+'\n')
        escrever.close()
    arquivo.close()