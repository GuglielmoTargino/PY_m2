# programa para verificar o alistamento
from datetime import date
data= date.today().year
genero=str(input('digite seu sexo. M para masculino ou F para feminino_'))

nasc=int(input('informe seu ano de nascimento_'))

calculo=data-nasc
if genero=='f':
    print('vc não precisa de alistamento')

elif calculo==18:
    print('Se aliste imediatamente')
elif calculo>18:
    saldo1=(data-nasc)-18
    print('vc deveria ter se alistado há {} anos'.format(saldo1))
elif calculo<18:
    saldo2=data-nasc
    print('vc não pode se alistar ainda. só tem {} anos'.format(saldo2))
else:
    print('vc não precisa se alistar')

print(' hoje é {}'.format(data))