# programa para adivinhar qual numero o computador escolheu

from random import randint
computador=randint(1,10)
jogador=int(input('Digite um número_'))
vezes=0

while computador!=jogador:
    jogador=int(input('Tente de novo_'))
    vezes+=1

    if jogador>computador:
        print('menos..')
    else:
        print('mais..')

print('Você tentou {} para acertar'.format(vezes))



