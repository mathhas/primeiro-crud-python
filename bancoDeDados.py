import mysql.connector
from pessoa import Pessoa

# Conexao com o banco de dados
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="pessoasPython"
)

# Interação com o banco de dados
mycursor = mydb.cursor()

#----------------------------------------Ações no DB-------------------------------------

# ------------------------Inserir-------------------


def inserirPessoaDB(pessoa):
    # comando
    sql = "INSERT INTO pessoas(nome, idade, cpf, cel) VALUES(%s, %s, %s, %s)"

    # valores
    val = (pessoa.nome, pessoa.idade, pessoa.cpf, pessoa.cel)

    # executa ação no db (mas não confirma a ação aplicando na tabela)
    mycursor.execute(sql, val)

    # aplica a execução, executando-a propriamente no db
    mydb.commit()


# ---------------------mostrar-dados-------------------

def mostrarPessoasDB():
    # comando
    sql = "SELECT * FROM pessoas"

    # executa ação
    mycursor.execute(sql)

    # salva tupla de pessoas cadastradas no DB na variavel pessoas
    pessoas = mycursor.fetchall()

    # exibe resultados
    for pessoa in pessoas:
        print(pessoa)

# ---------------------editar-dados-------------------


def editarPessoa(id, pessoa):
    # comando
    sql = "UPDATE pessoas SET nome = %s, idade = %s, cpf = %s, cel = %s WHERE id = %s"

    # valores
    val = (pessoa.nome, pessoa.idade, pessoa.cpf, pessoa.cel, id)

    # executa ação
    mycursor.execute(sql, val)

    # afetiva execução no DB
    mydb.commit()

# ---------------------deletar-pessoa-------------------


def deletarPessoa(id):
    # comando
    sql = "DELETE FROM pessoas WHERE id = %s"
    val = (id,)
    
    # executa ação
    mycursor.execute(sql, val)

    # efetiva a execução no DB
    mydb.commit()


def deletarPessoa(id):
    # comando
    sql = "DELETE FROM pessoas WHERE id = %s"
    val = (id,)
    
    # executa ação
    mycursor.execute(sql, val)

    # efetiva a execução no DB
    mydb.commit()
