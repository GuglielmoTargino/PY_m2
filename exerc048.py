#programa para somar todos os numeros impares de 1 a 100
soma=0
total=0
for c in range(1,100,2):
    if c%3 == 0:
        soma+=c
        total+=1
        print('os numeros são {}'.format(c))
print('total de numeros é {}'.format(total))
print(' a soma é {}'.format(soma))

