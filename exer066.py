#programa para criar uma sequencia de numeros que só para a contagem com 999

ctor=soma=0
while True:
    nr=int(input('digite_ ou 999 para parar_ '))
    if nr==999: # a flag é 999
        break
    soma+=nr
    ctor+=1
#print('foram digitados {}, e a soma é {}'.format(ctor,soma))
print(f'Foram digitados {ctor} numeros, e a soma é {soma}')# nova forma de imprimir na versão nova do pythom.
