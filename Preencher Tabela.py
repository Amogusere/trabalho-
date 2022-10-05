# Import required modules
import sqlite3
import csv

# Connecting to the geeks database
connection = sqlite3.connect('trabalho.db')
  
# Creating a cursor object to execute
# SQL queries on a database table
cursor = connection.cursor()
  
# Definições da Tabela Pessoas
create_table = '''CREATE TABLE pessoas(
                cpf TEXT NOT NULL,
                primeiro_nome TEXT NOT NULL,
                nome_do_meio TEXT NOT NULL,
                sobrenome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                id INTEGER PRIMARY KEY AUTOINCREMENT);
                '''
  
# Criando a tabela pessoas dentro do seu banco de dados 
cursor.execute(create_table)

# Definições da Tabela Contas
create_table = '''CREATE TABLE contas(
                agencia TEXT NOT NULL,
                numero TEXT NOT NULL,
                saldo TEXT NOT NULL,
                gerente TEXT NOT NULL,
                id_titular INTEGER PRIMARY KEY AUTOINCREMENT);
                '''
  
# Criando a tabela contas dentro do seu banco de dados 
cursor.execute(create_table)

FileRead = open("nomes.txt","r")
texto = ''
for line in FileRead:
    texto += line.replace(" ",",")
FileRead.close()
FileWrite = open("nomes.txt","w")
FileWrite.write(texto)
FileWrite.close()

FileRead = open("contas.txt","r")
texto = ''
for line in FileRead:
    texto += line.replace(" ",",")
FileRead.close()
FileWrite = open("contas.txt","w")
FileWrite.write(texto)
FileWrite.close()

# Abrindo o arquivo nomes.txt
file = open('nomes.txt')

# Lendo o conteúdo do arquivo nomes.txt
contents = csv.reader(file)

# SQL query para inserir dados dentro da tabela pessoas
insert_records = "INSERT INTO pessoas (cpf, primeiro_nome, nome_do_meio, sobrenome, idade, id) VALUES(?, ?, ?, ?, ?, ?)"

# Importando o conteúdo do arquivo txt para sua tabela pessoas
cursor.executemany(insert_records, contents)

# Abrindo o arquivo contas.txt
file = open('contas.txt')

# Lendo o conteúdo do arquivo contas.txt
contents = csv.reader(file)

# SQL query para inserir dados dentro da tabela contas
insert_records = "INSERT INTO contas (agencia, numero, saldo, gerente, id_titular) VALUES(?, ?, ?, ?, ?)"

# Importando o conteúdo do arquivo txt para sua tabela contas
cursor.executemany(insert_records, contents)

connection.commit()
connection.close()        
