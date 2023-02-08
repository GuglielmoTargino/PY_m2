#programa para contar quantas pessoas são de maior idade

from datetime import date
atual=date.today().year
iddmaior=0
iddmenor=0
for c in range(1,6):
    anopess=int(input('digite o ano de nascimento da {}° pessoa_'.format(c)))
    if (atual-anopess)>21:
        iddmaior+=1
    else:
        iddmenor+=1

print(' total maior idade é, {}, e total menor idade é {}'.format( iddmaior,iddmenor))



