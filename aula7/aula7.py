e_commerce = {

'secao':{

'tênis':{'Nike Air Max Invigor':600.0,'Nike TN':1000.0},
'camisa':{'Camisa Oficial do São Paulo Futebol Clube':600.0,'Camisa oficial do Liverpool': 900.0},
'acessorio':{'Cordão de Prata':50.0,'Pulseira de Prata':27.0},


}
}

compras = []
valor  = []
secao = input('Digite a seção: ')
prod1 =  input('Digite o produto: ')

secao = input('Digite a seção: ')
prod2 =  input('Digite o produto: ')

secao = input('Digite a seção: ')
prod3 =  input('Digite o produto: ')


compras.append(prod1)
compras.append(prod2)
compras.append(prod3)
print(compras)


valor.append(e_commerce['secao'][secao][prod1])
valor.append(e_commerce['secao'][secao][prod2])
valor.append(e_commerce['secao'][secao][prod3])

print('R$', valor)
soma  =  sum(valor)
print('R$', soma)





