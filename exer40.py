#Esse programa faz o calculo classico da média
nota1=float(input('digite a primeira nota_'))
nota2=float(input('digite a segunda nota_'))

media=(nota1+nota2)/2

if media >6:
    print('aluno APROVADO')
elif media > 5:
    print('aluno em RECUPERAÇÃO')
else:
    print('aluno REPROVADO')
