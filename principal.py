from pessoa import *
from bancoDeDados import *
from validacao import *
# FEITO INTEGRAÇÃO COM DB
# PRÓXIMO PASSO: REALIZAR VALIDAÇÕES#

inicio()
menu()

continua = True

while continua:
    inicio()
    menu()

    escolha = escolhaMenu()

    if escolha == '1':
        # Instancia pessoa
        pessoa = Pessoa(inputString('nome'), validaInt('nova'),
                        inputString('cpf'), inputString('celular'))
        # print(pessoa.__str__())
        inserirPessoaDB(pessoa)
        print('\nCadastro Efetuado corretamente!\n')
    elif escolha == '2':
        print('\nVeja a lista de pessoas cadastradas: ')
        mostrarPessoasDB()

        idPessEditar = str(
            input('\nDigite o id do usuário que deseja EDITAR: '))

        print('Mesmo que não deseje alterar um campo, escreva-o novamente. Do contrário, o campo ficará vazio.')

        pessoa = Pessoa(inputString('nome'), validaInt('nova'),
                        inputString('cpf'), inputString('celular'))

        editarPessoa(idPessEditar, pessoa)
        print('\nUsuário Editado!\n')
    elif escolha == '3':
        print('\nVeja a lista de pessoas cadastradas: ')

        mostrarPessoasDB()

        idPessDel = str(
            input('\nDigite o id do usuário que deseja DELETAR: '))

        deletarPessoa(idPessDel)
        print(f'\nUsuário de id: {idPessDel} DELETADO!\n')
    elif escolha == '4':
        mostrarPessoasDB()
    else:
        continua = False
