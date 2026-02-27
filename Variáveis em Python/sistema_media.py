print('Sistema de Verificação de Média')

nome = input('Digite o nome do aluno: ')

print('Digite as notas do aluno', nome)
n1 = float(input('Digite sua nota 1: '))
n2 = float(input('Digite sua nota 2: '))
n3 = float(input('Digite sua nota 3: '))
print('***' * 15)
print('Média do Aluno(a)', nome)
media = (n1 + n2 + n3) / 3
print('Média do Aluno(a)', nome)
print(round(media,2))


aprovado = media >= 7
recuperacao = media >=5 and media < 7
reprovado = media < 5

print(f'''
SITUAÇÃO DO ALUNO(A {nome}
      
Aprovado? - {aprovado}
Reprovada? - {reprovado}
Recuperação? - {recuperacao}

''')