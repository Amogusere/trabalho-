# Importando módulo requerido
import sqlite3

# Conectando o banco de dados
connection = sqlite3.connect('trabalho.db')

# Criando um objeto cursor para executar consulta SQL nas tabelas do banco de dados
cursor = connection.cursor()

ID = input("Digite o ID a ser deletado: ")

# SQL query para deletar dados dentro da tabela pessoas
Delete_records = "DELETE FROM PESSOAS WHERE ID = '"+ID+"'"
  
# Deletar dados na tabela pessoas 
cursor.execute(Delete_records)

# SQL query para deletar dados dentro da tabela contas
Delete_records = "DELETE FROM CONTAS WHERE ID_TITULAR = '"+ID+"'"
  
# Deletar dados na tabela contas 
cursor.execute(Delete_records)

print("Registro deletado!")

connection.commit()
connection.close() 