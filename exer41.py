# programa para analisar 5 condiçoes com if/else
from datetime import date
atual= date.today().year
nasc=int(input('digite seu ano de nascimento_'))
resultado= atual-nasc
if resultado >25:
    print('master')
elif resultado >=24:
    print('senior')
elif resultado >=19:
    print('junior')
elif resultado >=14:
    print('infantil')
else:
    print('mirim')

