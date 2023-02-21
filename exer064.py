# programa para se contar uma sequencia de numeros
num=int(input('Digite um numero, ou 999 para parar_'))
ctle=sma=0
while num!=999:
    sma+=num
    num=int(input('digite um numero ou 999 para parar_'))
    ctle+=1
    
print('vc digitou {} e a soma é {}'.format(ctle,sma))

