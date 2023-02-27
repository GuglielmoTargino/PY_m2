#programa para analisar dados de uma compra.
maior=menor=ctdr=soma=qtd=0
nmprod=' '
# maior guarda maior valor
#menor guarda menor valor
#ctdr contador para entrada de produtos
#soma guarda soma dos produtos
#qtd guarda quantos produtos custaram mais de R$1000.00 

while True:
    bda=' '# bandeira recebe SIM ou NÃo do usuário para continua
    prod=str(input('Digite o produto_')).strip()
    pco=float(input('Digite o perço do produto R$_'))
    soma+=pco
    ctdr+=1
    if ctdr==1:# se o valor for o inicial. seta menor com o valor digita.
        menor=pco
        nmprod=prod
    if pco>maior:# armazena o maior valor
        maior=pco
    if pco<menor:#armazena o menor valor
        menor=pco
        nmprod=prod
    if pco>1000:
        qtd+=1

    while bda not in 'SN': # filtro linha para contra digitação errada do usuario
        bda=str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    
    if bda=='N':
        break
print('='*20)
print(f'Total foi R${soma}')
print(f'O maior valor foi {maior}, e o menor valor foi {menor}')
print(f'O produto mais barato foi {nmprod} por R${menor}')
print(f'Teve {qtd} prod. com valor acima de R$1000.00')
print('Fim programa_')
