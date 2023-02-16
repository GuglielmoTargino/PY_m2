# programa para escolher uma base de conversão numérica
num=int(input('digite um numero inteiro_'))
print('escolha a base numerica para conversão')
base=int(input('1-binario; 2-octa decimal; 3-hexadecimal'))
if base == 1:
    print('vc escolheu binario! {}'.format(bin(num)[2:]))
elif base == 2:
    print('vc escolheu octa decimal {}'.format(oct(num)[2:]))

elif base == 3:
    print('vc escolheu hexadecimal {}'.format(hex(num)[2:]))
else:
    print('escolha uma base.')

