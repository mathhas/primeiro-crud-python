class Pessoa:
    # -----------------------------------Atributos-------------------------------
    __id = int()
    __nome = str()
    __idade = int()
    __cpf = str()
    __cel = str()
    # ("__"no início da palavra é um tipo de encapsulamento em python (oculta o atributo para
    # acesso em outras classes ou métodos))

    # ------------------------------------Métodos----------------------------------

    # construtor
    def __init__(self, nome, idade, cpf, cel):
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf
        self.__cel = cel

    # getters
    @property
    def nome(self):
        return self.__nome
        # como tem esse getter para obter o nome da pessoa
        # é possível acessá-lo em outras classes. se não tivesse
        # também seria possível acessá-lo, porém com a seguinte sintaxe:
        #         objeto._NomeDaClasse__atributo

    @property
    def id(self):
        return self.__id

    @property
    def idade(self):
        return self.__idade

    @property
    def cpf(self):
        return self.__cpf

    @property
    def cel(self):
        return self.__cel

    # setters
    @nome.setter
    def nome(self, nome):
        # checar se é o tipo correto. se não for, validar;
        if isinstance(nome, str):
            self.__nome = nome
    # apenas para fim de padronização

    # funcionalidades de pessoa

    def cumprimentar(self):
        print(
            f'Olá eu me chamo: {self.__nome}! Tenho {self.__idade} anos e você?')

    # Sobrescrita do str (semelhante a sobrescrita do toString() em java)
    def __str__(self):
        return self.__nome, self.__idade, self.__cel
