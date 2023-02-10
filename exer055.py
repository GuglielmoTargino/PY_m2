#programa para se verificar o maior e o menor numero de uma lista

maior=0
menor=0

for p in range(1,4): #linha para verificar o maior numero
    pso=int(input('digite o peso da {}º pessoa_'.format(p)))
    if pso>maior:
        maior=pso
    if pso<maior:
        menor=pso



print(' o peso maior é {}'.format(maior))
print(' o menor numero é {}'.format(menor))




