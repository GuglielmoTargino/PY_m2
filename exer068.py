
# programa para um usuario jogar p\r ou imp\r com o computador

from random import randint
ctdor=0

while True:
    cpdor=randint(1,10)
    jdor=int(input('Digite um numero entre 1 e 10_'))
    dsao=str(input('Escolha par ou ímpar [P/I]?_')).strip().upper()[0]
    print(f'Jogador tirou {jdor} e decidiu {dsao}. Computador tirou {cpdor}')
    soma=jdor+cpdor

    if soma%2==0: # linha para marcar o resultado par ou impar
        res='P'
    else:
        res="I"

    if dsao==res: # linha para saber quem ganhou
        ctdor+=1
        print('jogador ganhou')
        
    else:
        print('Computador ganhou.')
        break
print(f'Fim. Vc ganhou {ctdor} vezes')