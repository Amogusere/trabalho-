import os
from pathlib import Path


print("qual consulta deseja fazer? se for gerente digite 1, se for CPF digite 2")

número = input("digite o número(1 ou 2): ")


if número == "1":
        gerente = input("informe o nome do arquivo: ")
        pasta = "Consulta gerente/"
        Directory = Path(pasta)
        file = Directory / gerente
        arq= open(file, 'r') 
        conteudo = arq.read() 
        print(conteudo)

elif número == "2":
        CPF = input("informe o nome do arquivo: ")
        pasta1 = "Consulta cpf/"
        Directory1 = Path(pasta1)
        file1 = Directory1 / CPF
        arq1= open(file1, 'r') 
        conteudo1 = arq1.read() 
        print(conteudo1) 
else:
    print("número diferente de 1 ou 2")