cadastros =  {}

cliente1 = input('Nome: ')
idade1 = input('Idade: ')
senha1 = input('Senha: ')

cliente2 = input('Nome: ')
idade2 = input('Idade: ')
senha2 = input('Senha: ')

cliente3 = input('Nome: ')
idade3 = input('Idade: ')
senha3 = input('Senha: ')

cadastros['nomes'] = [cliente1, cliente2, cliente3]
cadastros['idades'] = [idade1, idade2, idade3]
cadastros['senhas'] = [senha1, senha2, senha3]

print(cadastros)


login = input('Digite seu nome >>')
senha = input('Digite sua senha >>')


if login in cadastros ['nomes'] and senha in cadastros['senhas']:
    print('Seja muito bem-vindo(a)!')

    print('Opções de hospedagem: ', cadastros['nomes'][0])
    quartos = ['', 'Quarto Simples', 'Quarto Duplo', 'Quarto Luxo']
    precos = ['', 250,500, 1000]
    print('quartos: ', quartos)
    opcoes = int(input('1-Quarto Simples|2-Quarto Duplo| 3-Quarto de Luxo'))
    duracao_estadia = int(input('Dias de hospedagem '))
    cont = duracao_estadia * precos[opcoes]
    print('Você escolheu o quarto: ', quartos[opcoes], 'Dias de hospedagem: ', duracao_estadia)
    print('Valor a cobrar R$', round(cont,2))

    print('Opções de hospedagem: ', cadastros['nomes'][1])
    quartos = ['', 'Quarto Simples', 'Quarto Duplo', 'Quarto Luxo']
    precos = ['', 250,500, 1000]
    print('quartos: ', quartos)
    opcoes = int(input('1-Quarto Simples|2-Quarto Duplo| 3-Quarto de Luxo'))
    duracao_estadia = int(input('Dias de hospedagem '))
    cont = duracao_estadia * precos[opcoes]
    print('Você escolheu o quarto: ', quartos[opcoes], 'Dias de hospedagem', duracao_estadia)
    print('Valor a cobrar R$', round(cont,2))

    print('Opções de hospedagem: ', cadastros['nomes'][2])
    quartos = ['', 'Quarto Simples', 'Quarto Duplo', 'Quarto Luxo']
    precos = ['', 250,500, 1000]
    print('quartos: ', quartos)
    opcoes = int(input('1-Quarto Simples|2-Quarto Duplo| 3-Quarto de Luxo'))
    duracao_estadia = int(input('Dias de hospedagem '))
    cont = duracao_estadia * precos[opcoes]
    print('Você escolheu o quarto: ', quartos[opcoes], 'Dias de hospedagem', duracao_estadia)
    print('Valor a cobrar R$', round(cont,2))

else:
    print('Acesso Inválido, cadastre-se novamente!')