
#programa para se calcular uma PA até o decimo termo.
termo=int(input('digite o primeiro termo da PA_'))
raz=int(input('agora digite a razão da PA_'))
fim=int(input('agora digite o enesimo termo de parada_'))
decimo=termo+((fim-1)*raz) # formula para se calcular o decimo termo. 

for c in range(termo,decimo+raz,raz):
    print(' a PA é {}'.format(c))



