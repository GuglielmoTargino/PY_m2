#programa para analisar um triangulo
reta1=int(input('digite o tamanho da primeira reta do triangulo_'))
reta2=int(input('digite o tamanho da segunda reta do triangulo_' ))
reta3=int(input('digite o tamanho da terceira reta do triangulo_'))

if reta1<reta2+reta3 and reta2<reta1+reta3 and reta3<reta1+reta2:
    print('retas {}, {} e {} formam um triangulo'.format(reta1,reta2,reta3))
    if reta1==reta2 and reta1==reta3:
        print('triangulo equilátero')
    elif reta1!=reta2 and reta1!=reta3 and reta3!=reta2:
        print('triangulo escaleno')
    else:
        print('triangulo isosceles')
    
else:
    print('retas {},{} e {} não formam umtriangulo'.format(reta1,reta2,reta3))

