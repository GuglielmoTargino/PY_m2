#programa do jogo joquenpo
from random import randint
from time import sleep
itens=('tesoura','papel','pedra')
computador=randint(0,2)
print('computador escolheu {}_____'.format(itens[computador]))
jogador=int(input('''digite uma opção
[0] tesoura
[1] papel
[2] pedra
 '''))

print('JO')
sleep(1)
print('kem')
sleep(1)
print('pô')
sleep(1)

print('jogador escolheu {}____'.format(jogador))
if computador==jogador:
    print('empate')
elif computador==0:
    if jogador==1:
        print('computador ganhou')
    else:
        print('jogador ganhou')
elif computador==1:
    if jogador==2:
        print('computador ganhou')
    else:
        print('jogador ganhou')

elif computador==2:
    if jogador==0:
        print('computador ganhou')
    else:
        print('jogador ganhou')


    
