# programa para analisar uma lista de pesoas

idadehome=0
pesomulher=0
somaidade=0
contidade=0
media=0
nomehomem=''
contmulher=0


for p in range(1,5):
    pessoa=str(input('Digite o nome da {} pessoa_'.format(p)))
    sexo=str(input('Digite o sexo M/F_'))
    idade=int(input('Dgite a idade_'))
    somaidade+=idade
    media=somaidade/3

    if sexo in('Mm') and idade>idadehome:
       
            idadehome=idade
            nomehomem=pessoa

    if sexo in ('Ff') and idade<20:
        contmulher+=1




print('O homem mais velho registrado foi {} com {} de idade'.format(nomehomem,idadehome))
print('A média de idade é igual a {:.1f}'.format(media))
print('A quantidade de mulheres com idade menor que 20 anos é {}'.format(contmulher))







