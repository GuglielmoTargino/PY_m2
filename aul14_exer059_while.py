#programa para se montar um menu de opções entre dois numeros
n1=int(input('digite o primeiro numero_'))
n2=int(input('digite o segundo numero_'))
opcao=0
resultado=0


while opcao!=5:
    print('''escolha a opcao 
    [1]soma
    [2]multiplica
    [3]maior
    [4]novos numeros
    [5]sair''')
    opcao=int(input(''))

    if opcao==1:
        soma=n1+n2
        print('A soma é {}'.format(soma))
    

    if opcao==2:
        resultado=n1*n2
        print('A multiplicação é {}'.format(resultado))

    if opcao==3:
        if n1>n2:
            maior=n1
        else:
            maior=n2
        print('O maior numero é {}'.format(maior))

    if opcao==4:
        n1=int(input('digitep primeiro numero de novo_'))
        n2=int(input('digite segundo numero novo_'))

    if opcao==5:
        print('<<<<<< Programa finalizado >>>>>>')

print('Volte sempre')
