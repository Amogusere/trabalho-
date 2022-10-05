# Importando módulo requerido
import sqlite3

# Conectando o banco de dados
connection = sqlite3.connect('trabalho.db')

# Criando um objeto cursor para executar consulta SQL nas tabelas do banco de dados
cursor = connection.cursor()

ID = input("Digite o ID a ser Editado: ")

# SQL query para selecionar dados dentro da tabela pessoas
Select_records1 = "SELECT * FROM PESSOAS WHERE ID = '"+ID+"'"
  
# Selecionar dados na tabela pessoas 
cursor.execute(Select_records1)
print(cursor.fetchall())

# SQL query para selecionar dados dentro da tabela contas
Select_records2 = "SELECT * FROM CONTAS WHERE ID_TITULAR = '"+ID+"'"
  
# Deletar dados na tabela contas 
cursor.execute(Select_records2)
print(cursor.fetchall())

print("Editar dados!")
cpf = input("Digite o CPF: ")
primeiro_nome = input("Digite o Primeiro Nome: ")
nome_do_meio = input("Digite o Nome do Meio: ")
sobrenome = input("Digite o Sobrenome: ")
idade = input("Digite a Idade: ")
agencia = input("Digite a Agência: ")
numero = input("Digite o Número da Conta: ")
saldo = input("Digite o Saldo: ")
gerente = input("Digite o Gerente: ")

# SQL query para atualizar dados dentro da tabela pessoas
Update_records = "UPDATE PESSOAS SET cpf = '"+cpf+"', primeiro_nome = '"+primeiro_nome+"', nome_do_meio = '"+nome_do_meio+"', sobrenome = '"+sobrenome+"', idade = '"+idade+"' WHERE ID = '"+ID+"'" 

# Atualizar dados na tabela pessoas 
cursor.execute(Update_records)

# SQL query para atualizar dados dentro da tabela contas
Update_records = "UPDATE CONTAS SET agencia = '"+agencia+"', numero = '"+numero+"', saldo = '"+saldo+"', gerente = '"+gerente+"' WHERE ID_TITULAR = '"+ID+"'"
  
# Atualizar dados na tabela contas 
cursor.execute(Update_records)

print("Registro atualizado!")

connection.commit()
connection.close() 