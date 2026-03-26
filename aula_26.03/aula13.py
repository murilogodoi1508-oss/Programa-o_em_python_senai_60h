#1
import random

num1 = random.randint(5,10)
print(num1)

#2
num2 = [random.randint(1, 100) for _ in range(3)]
print(num2)





#3
num3 = [random.randint(10, 30) for _ in range(1)]
print(num3)






#4
import time
for i in range(10, 0, -1):
    print(i)
    time.sleep(1)

print('Fogo!!')


#5
soma = 0

for num4 in range(1, 101):
    if num4 % 2 == 0:
        soma += num4

print("A soma dos números pares é:", soma)





#6
num5 =  int(input('Digite um número para saber a tabuada: '))
print(f'tabuada do {num5}:')

for i in range(1,11):
    print(f'{num5} x {i} = {num5 * i}')

















#7

print("Números ímpares de 99 a 1:")

for i in range(99, 0, -2): 
    print(i)



