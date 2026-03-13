#Atividade 1
#1
mil = 0

while mil <= 1000:
    print(mil)
    mil = mil + 1

#2
nomes = []


c = 10
while c >0:
    n = input('nomes: ')
    nomes.append(n)
    print(nomes)

    c = c - 1

 


#Atividade 2

senha_padrao = '1020'
tentativas = 3
while tentativas > 0:
    senha_usuario = input('Digite a sua senha: ')
    tentativas = tentativas -1
    if  senha_usuario == senha_padrao:
        print('Senha Correta!!')
        print('notas: ')
        nota1 = int(input('Digite a nota 1:'))
        nota2 = int(input('Digite a nota 2:'))
        nota3 = int(input('Digite a nota 3:'))

        media = (nota1+nota2+nota3) / 3
        media_arredondada = round(media, 2)
        print ({media_arredondada})

else:
        print('Conta Bloqueada!!')



   
