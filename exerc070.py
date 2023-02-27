#programa para analisar dados de uma compra.
maior=menor=ctdr=soma=qtd=0
nmprod=' '

while True:
    bda=' '
    prod=str(input('Digite o produto_')).strip()
    pco=float(input('Digite o perço do produto R$_'))
    soma+=pco
    ctdr+=1
    if ctdr==1:
        menor=pco
        nmprod=prod
    if pco>maior:
        maior=pco
    if pco<menor:
        menor=pco
        nmprod=prod
    if pco>1000:
        qtd+=1

    while bda not in 'SN':
        bda=str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    
    if bda=='N':
        break
print('='*20)
print(f'Total foi R${soma}')
print(f'O maior valor foi {maior}, e o menor valor foi {menor}')
print(f'O produto mais barato foi {nmprod} por R${menor}')
print(f'Teve {qtd} prod. com valor acima de R$1000.00')
print('Fim programa_')
