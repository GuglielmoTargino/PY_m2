# programa para validação de informação
sexo='g'
while sexo not in ('MF'):
    sexo=str(input('digite seu sexo M/F_')).strip().upper()[0]

print('o sexo digitado foi {}'.format(sexo))
