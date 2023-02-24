
tb=int(input('Digite qual tabuada vc quer saber_'))
ctor=0  # contador iiciado em zero

while tb>0: 

    while ctor<10:
        ctor+=1
        prod=tb*ctor
        print('{} x {} = {}'.format(tb,ctor,prod))
    tb=int(input('Digite outra tabuada? Ou digite um numero negativo para sair_'))
    ctor=0 #linha para zerar o contador e começar de novo o loop
print('Fim Tabuada')








