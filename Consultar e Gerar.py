# Importando módulo requerido
import sqlite3
from msilib.schema import Directory
import os.path
from pathlib import Path
from datetime import datetime
import time
import csv
conteudo = []
conteudo2 = []
# Conectando o banco de dados
connection = sqlite3.connect('trabalho.db')

# Criando um objeto cursor para executar consulta SQL nas tabelas do banco de dados
cursor = connection.cursor()

cpf = input("Digite o CPF para consulta: ") 

# SQL query para selecionar dados dentro da tabela pessoas

Select_records1 = "SELECT * FROM PESSOAS WHERE cpf = '"+cpf+"'" 
 
# Selecionar dados na tabela pessoas 
Nome1 = cursor.execute(Select_records1)

# Criar pasta 
pasta = "Consulta cpf/"
if os.path.isdir(pasta): # vemos de este diretorio ja existe
        print ('Ja existe uma pasta com esse nome!')
else:
        os.mkdir(pasta) # aqui criamos a pasta caso nao exista
        print ('Pasta criada com sucesso!')
                

# Criar arquivo txt e inserir dados da consulta
timestr = datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p")
NomeArq = 'cpf-'+timestr+'.txt'
Directory = Path(pasta)
file = Directory / NomeArq
for row in Nome1:
    conteudo.append(row)
arquivo = open(file,'w')
arquivo.writelines(str(conteudo))
arquivo.close()

gerente = input("Digite o gerente da conta para consulta: ") 

# SQL query para selecionar dados dentro da tabela pessoas

Select_records2 = "SELECT * FROM CONTAS WHERE gerente = '"+gerente+"'" 
 
# Selecionar dados na tabela pessoas 
Nome2 = cursor.execute(Select_records2)

# Criar pasta 
pasta2 = "Consulta gerente/"
if os.path.isdir(pasta2): # vemos de este diretorio ja existe
        print ('Ja existe uma pasta com esse nome!')
else:
        os.mkdir(pasta2) # aqui criamos a pasta caso nao exista
        print ('Pasta criada com sucesso!')
                

# Criar arquivo txt e inserir dados da consulta
timestr2 = datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p")
NomeArq2 = 'gerente-'+timestr2+'.txt'
Directory2 = Path(pasta2)
file2 = Directory2 / NomeArq2
for row2 in Nome2:
    conteudo2.append(row2)
arquivo2 = open(file2,'w')
arquivo2.writelines(str(conteudo2))
arquivo2.close()


connection.commit()
connection.close() 