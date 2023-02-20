# programa para calcular o fatorial e um número
n1=int(input('Digite um numero para saber o fatorial dele_'))
fat=1
n=n1
while n> 0:
    print('{}'.format(n))
    fat*=n
    n-=1
print('O fatorial de {} é {}.'.format(n1,fat))
