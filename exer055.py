#programa para se verificar o maior e o menor numero de uma lista

maior=0
menor=0

for p in range(1,4): #linha para verificar o maior numero
    pso=int(input('Digite o peso da {}º pessoa em Kg_'.format(p)))

    if p==1:
        menor=pso # linha para tirar a variável menor do valor 0. 

    if pso>maior:
        maior=pso

    if pso<maior:
        menor=pso



print('O maior peso registrado foi {}Kg'.format(maior))
print('O menor peso registrado foi {}Kg'.format(menor))




