import statistics
empresa1 = [1000,6000,1200,8000,1400]
empresa2 = [5000,4000,3000,2000,7000]
empresa3 = [1200,1300,8000,3000,15000]
empresa4 = [1400,1750,2000,4500,5900]

media1 = statistics.mean(empresa1)
moda1 = statistics.mode(empresa1)
mediana1 = statistics.median(empresa1)
desvio_padrao1 = statistics.stdev(empresa1)

print("\nEmpresa 1")
print("Média:", media1)
print("Mediana:", mediana1)
print("Moda:", moda1)
print("Desvio padrão:", round(desvio_padrao1,2))


media2 = statistics.mean(empresa2)
moda2 = statistics.mode(empresa2)
mediana2 = statistics.median(empresa2)
desvio_padrao2 = statistics.stdev(empresa2)

print("\nEmpresa 2")
print("Média:", media2)
print("Mediana:", mediana2)
print("Moda:", moda2)
print("Desvio padrão:", round(desvio_padrao2,2))

media3 = statistics.mean(empresa3)
moda3 = statistics.mode(empresa3)
mediana3 = statistics.median(empresa3)
desvio_padrao3 = statistics.stdev(empresa3)

print("\nEmpresa 3")
print("Média:", media3)
print("Mediana:", mediana3)
print("Moda:", moda3)
print("Desvio padrão:", round(desvio_padrao3,2))

media4 = statistics.mean(empresa4)
moda4 = statistics.mode(empresa4)
mediana4 = statistics.median(empresa4)
desvio_padrao4 = statistics.stdev(empresa4)

print("\nEmpresa 4")
print("Média:", media4)
print("Mediana:", mediana4)
print("Moda:", moda4)
print("Desvio padrão:", round(desvio_padrao4,2))

print(f'A melhor escolha é: Empresa 3 (Melhor opção de valores!)')

