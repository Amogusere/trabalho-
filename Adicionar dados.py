# Import required modules
import sqlite3

# Connecting to the geeks database
connection = sqlite3.connect('trabalho.db')

# Creating a cursor object to execute
# SQL queries on a database table
cursor = connection.cursor()

cpf = input("Digite o CPF: ")
primeiro_nome = input("Digite o Primeiro Nome: ")
nome_do_meio = input("Digite o Nome do Meio: ")
sobrenome = input("Digite o Sobrenome: ")
idade = input("Digite a Idade: ")
agencia = input("Digite a Agência: ")
numero = input("Digite o Número da Conta: ")
saldo = input("Digite o Saldo: ")
gerente = input("Digite o Gerente: ")

# SQL query para inserir dados dentro da tabela pessoas
insert_records = "INSERT INTO pessoas (cpf, primeiro_nome, nome_do_meio, sobrenome, idade) VALUES('"+cpf+"', '"+primeiro_nome+"', '"+nome_do_meio+"', '"+sobrenome+"', '"+idade+"')"
  
# Gravar novos dados na tabela pessoas 
cursor.execute(insert_records)

# SQL query para inserir dados dentro da tabela contas
insert_records = "INSERT INTO contas (agencia, numero, saldo, gerente) VALUES('"+agencia+"', '"+numero+"', '"+saldo+"', '"+gerente+"')"
  
# Gravar novos dados na tabela contas 
cursor.execute(insert_records)

connection.commit()
connection.close()        
