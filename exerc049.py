#tabuada usando laço for 

num=int(input('digite um numero para saber a tabuada_'))

for g in range(1,11):
    tabu=num*g
    print('{} X {} = {}'.format(num, g,tabu))
