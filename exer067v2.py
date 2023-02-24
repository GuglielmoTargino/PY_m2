#programa de tabuada com laço while e ponto de parada break
while True:
    tb=int(input('Digite a tabuada. Ou um número negativo para sair_'))
    if tb<0:
        break
    for c in range(1,11):
        print(f'{tb} x {c} = {tb*c}')

print('Número negativo digitado. Fim tabuada')