def validaInt(txt=''):
    erro = True
    while erro:
        erro = False
        try:
            inteiro = int(input(f'Digite a {txt} idade da pessoa: '))
        except:
            erro = True
            print('ERRO! digite apenas números inteiros!')
    return inteiro


def inputString(txt):
    texto = str(input(f'Digite o {txt} da pessoa: '))
    return texto


def escolhaMenu():
    escolha = str(
        input('\nEscolha uma das opções acima para continuar com o programa: ')).strip().upper()
    while escolha != '1' and escolha != '2' and escolha != '3' and escolha != '4' and escolha != '0':
        escolha = str(
            input('\nEscolha uma válida para continuar com o programa! tente novamente: ')).strip().upper()
    return escolha

def menu():
    print('1 - Cadastrar pessoa')
    print('2 - editar pessoa')
    print('3 - deletar pessoa')
    print('4 - mostrar pessoas cadastradas')
    print('0 - encerrar programa')


def inicio():
    print('=-'*40)
    print('-------------------------------------INÍCIO-------------------------------------')
    print('=-'*40)
    print('\nEste programa é um simples CRUD de pessoas para efeito de treinamento:\n')
