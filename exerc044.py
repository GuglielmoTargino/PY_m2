#programa para calcular o imc
alt=float(input('informe sua altura em metros_'))
peso=float(input('informe seu peso em KG_'))
imc=peso/(alt**2)

if imc>40:
    print('obesidade morbida')
elif imc>30:
    print('obesidade')
elif imc>25:
    print('sobrepeso')
elif imc>18.5:
    print('peso ideal')
else:
    print('abaixo do peso')
