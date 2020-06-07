from pessoa import Pessoa
from bancoDeDados import *

# FEITO INTEGRAÇÃO COM DB
# PRÓXIMO PASSO: REALIZAR VALIDAÇÕES#


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


continua = True

while continua:
    inicio()
    menu()

    escolha = str(
        input('\nEscolha uma das opções acima para continuar com o programa: ')).strip().upper()
    while escolha != '1' and escolha != '2' and escolha != '3':
        escolha = str(
            input('\nEscolha uma válida para continuar com o programa! tente novamente: ')).strip().upper()

    if escolha == '1':
        # Instancia pessoa
        pessoa = Pessoa(input('Digite o nome da pessoa: '), input('Digite a idade da pessoa: '), input(
            'Digite o cpf da pessoa: '), input('Digite o celular da pessoa: '))
        print(pessoa.__str__())
        inserirPessoaDB(pessoa)
    elif escolha == '2':
        print('\nVeja a lista de pessoas cadastradas: ')
        mostrarPessoasDB()
        idPessEditar = str(
            input('\nDigite o id do usuário que deseja EDITAR: '))
        print('Mesmo que não deseje alterar um campo, escreva-o novamente. Do contrário, o campo ficará vazio.')
        pessoa = Pessoa(input('Digite o novo nome da pessoa: '), input('Digite a nova idade da pessoa: '), input(
            'Digite o cpf da pessoa: '), input('Digite o novo celular da pessoa: '))
        editarPessoa(idPessEditar, pessoa)
    elif escolha == '3':
        print('\nVeja a lista de pessoas cadastradas: ')
        mostrarPessoasDB()
        idPessDel = str(
            input('\nDigite o id do usuário que deseja DELETAR: '))
        deletarPessoa(idPessDel)
    elif escolha == '4':
        mostrarPessoasDB()
    else:
        continua = False
