#vprograma para somar so os numeros pares
contador=0
tot=0

for c in range(1,9):
    num=int(input('digite o {}º numero_'.format(c)))
    if num%2 ==0:
        contador=contador+num
        tot=tot+1

print('vc digitou {} numeros pares'.format(tot))
print('A soma deles é {}'.format(contador))


