#1
def compara_par_impar(num1, num2):
    
    res1 = "par" if num1 % 2 == 0 else "ímpar"
    res2 = "par" if num2 % 2 == 0 else "ímpar"
    
    print(f"O número {num1} é {res1}.")
    print(f"O número {num2} é {res2}.")
    
   
    if num1 > num2:
        return f"{num1} é maior que {num2}"
    elif num2 > num1:
        return f"{num2} é maior que {num1}"
    else:
        return "Os números são iguais"


resultado_comparacao = compara_par_impar(10, 7)
print(resultado_comparacao)



#2
def mult():
    print(3*4*5)


#3
def elevado():
  n3  = 10
  n4 = int(input('valor elevado'))
  print(n3**n4)



#4
def verificando_idade():
    idade =  int(input('idade: '))
    if idade == 18:
        print('18  anos')
    else:
        print('Não tem 18')


#5
def mostrar_ano():
    ano_atual = 2025
    ano_nascimento = int(input('Ano nascimento:'))
    mes =  int(input('digite o numero do mês 1'))
    cal  =  2025 - ano_nascimento

    if mes <=6:
        print('Ano nascimento', cal)
    else:

         print('Ano nascimento', cal - 1)




#6 
def verificar():
    copas = [1958,1962,1970,1994,2002]

    ano =  int(input('Digite o ano que vc acha que o br granhou'))
    if ano in copas:
        print('ganhou!')
    else:
        print('Não ganhou!')



#7
def cumprimento(nome):
    return 'olá', nome

def produto(lista_prod, prod, carrinho, meus_v, lista_valores, paga):

    carrinho.append(lista_prod[prod])
    meus_v.append(lista_valores[paga])
    return carrinho,'R$',  float(sum(meus_v))


def pagamento(lista_tip_pags, escolha_pag):
    return lista_tip_pags[escolha_pag]




def restaurante():
   
    menu = ['','SALADA', 'MACARRONADA', 'SANDUICHE', 'SORVETE']
    valores  = [0,100,60,150,250]
    carrinho = []
    meus_valores = []
    nome = input('Nome: ')
    print(cumprimento(nome))
 
    for p, v in enumerate(zip(menu, valores)):
        print(p,'R$', v)    

    acrescentar =  input('deseja acrescentar ao carrinho? ')
    while acrescentar == 'sim':    
        e  =  int(input('Escolha seu produto: 1 ,2 ,3, 4'))
        print( produto(menu, e, carrinho, meus_valores,valores, e ))
        acrescentar = input('Deseja continuar? ')
 
    else:
        lista_pag = ['', '1 pix', '2 CC', ' 3 CD']
        escolha =  int(input(f'Escolha a forma de pagamento,  {lista_pag}'))
        print(pagamento(lista_pag, escolha))
        print('Obrigado volte SEMPRE!')    
