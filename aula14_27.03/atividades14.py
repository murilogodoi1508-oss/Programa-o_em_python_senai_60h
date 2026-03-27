#1
import os

with open('teste.txt', 'w') as conteudo:
    c = conteudo.read()
    
    print(c)


with open('teste.txt', 'r') as conteudo:
    c = conteudo.read()
    
    print(c)


#2
os.mkdir("meu_diretorio")

#3
os.rename("meu_diretorio", "novo_diretorio")


#4
with os.scandir('meu_diretorio') as entrada:
    for teste in entrada:
        if teste.is_file():
            print(f'Arquivo encontrado: {teste.name}')


#5
import shutil

shutil.copytree("teste.txt", "novo_diretorio/teste_copia.txt")


#6
import os

os.remove("teste.txt")