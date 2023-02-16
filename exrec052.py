#programa para descobrir se um numero é primo
num=int(input('digite um numero_'))
saldo=0

for c in range(1,num+1):
    if num%c==0:
        saldo=saldo+1
if saldo>3:
    print('o numero {} não é primo.'.format(num))
else:
    print(' {} é um numero primo.'.format(num))


