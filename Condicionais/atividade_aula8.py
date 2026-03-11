#Exercicios
#1
numero = int(input('Digite um numero: '))

if numero >0:
    print('Positivo')
elif numero <0:
    print('Negativo')
else:
    print('Zero')


#2
idade = int(input('Digite sua idade: '))

if idade >16:
    print('Você pode votar!')
elif idade <16:
    print('Você não pode votar.')


#3
num1 = int(input('Digite um numero: '))
if num1 % 2 == 0:
    print('O numero é par')
else: print('O numero é impar')







#4
num2 = int(input('Digite o primeiro numero: '))
num3 = int(input('Digite o segundo numero: '))
num4 = int(input('Digite o terceiro numero: '))

if num2 == num3 == num4 == num2:
    print('Equilátero')
elif num2 != num3 == num4 != num2:
    print('Isósceles')
else: 
    print('Escaleno')


#5
num5 = int(input('Digite um numero: '))
if num5 % 7 == 0 and num5 % 5 ==0:
    print('Divisivel')
else:
    print('Não é divisivel')


#6
num6 = int(input('Digite um numero: '))

if num6 >10:
    print(f"O número {num6} é positivo e maior que 10.")
elif num6 >0:
    print(f"O número {num6} é positivo, mas não é maior que 10.")
elif num6 == 0:
    print("O número é zero.")
else:
    print(f"O número {num6} é negativo.")


#7

num7 = int(input("Digite um número: "))


if num7 % 3 == 0 or num7 % 5 == 0:
    print(f"{num7} é divisível por 3 ou 5.")
else:
    print(f"{num7} não é divisível por 3 nem por 5.")




