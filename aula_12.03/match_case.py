#1

num1 = 10

match num1 % 2 == 0:
    case 0:
        print("Par")
    case 1:
        print("Ímpar")




#2
num2 = 15

match num2:
    case num2 if num2 > 0:
        print("Positivo")
    case num2 if num2 < 0:
        print("Negativo")
    case _:
        print("Zero")



#3
palavra = ""

match palavra:
    case "":
        print("A string está vazia.")
    case _:
        print("A string possui conteúdo.")




#4
num3 = 35

match True:
    case _ if num3 > 10:
        print("Maior que 10")
    case _ if num3 < 10:
        print("Menor que 10")
    case _ if num3 == 10:
        print("Igual a 10")
    case _:
        print("Valor inválido")




#5
idade = 30 

match idade:
    case i if i <= 12:
        classificacao = 'Criança'
    case i if i <= 17:
        classificacao = 'Adolescente'
    case i if i <= 34:
        classificacao = 'Jovem'
    case i if i <= 64:
        classificacao = 'Adulto'
    case _:
        classificacao = 'Idoso'

print(f'A idade {idade} é classificada como: {classificacao}')


