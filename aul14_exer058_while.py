# programa para adivinhar qual numero o computador escolheu

from random import randint
computador=randint(1,10)
print('computador escolheu {}'.format(computador))
print('Digite um numero entre 0 e 10.')
jogador=int(input(''))
vezes=1

while computador!=jogador:
    #jogador=int(input('Tente outra vez_'))
    vezes+=1
    if jogador>computador:
        print('É menos...')
    else:
        print('É mais...') 
    jogador=int(input('Tente de novo_'))  

print('Você tentou {} vezes para acertar.'.format(vezes))



