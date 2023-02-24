#programa para analisar dados de uma lista de pessoas cadastradas

ctdora=ctdoro=ctdorm=ctdorg=0
while True:
    idade=int(input('digite a idade em anos_'))
    sexo=str(input('digite o sexo [M/F]')).strip().upper()[0]
    ctdorg+=1 # contador geral de pessoas inseridas

    if idade>18: # linha para contar os maiores de idade
        ctdora+=1

    if sexo=="M": #linha para incrementar o contador masculino
        ctdoro+=1
    elif idade<20: #linha para incrementar o conyador feminino menor de 18 anos de idade
        ctdorm+=1
    bda=str(input('deseja continuar?_[S/N]')).strip().upper()[0] # #linha para flag de parada

    if bda=='N':
        break
print(f'tota cadastrado foi {ctdorg}')
print(f'{ctdora} Tem mais de 18 anos de idade')
print(f'{ctdoro} são do sexo masculino')
print(f'{ctdorm} sao do sexo feminino menores de 20 anos de idade')