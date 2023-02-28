# programa para simular uma contagem de notas para saque em um ATM

saque=int(input('Digite quanto vc que sacar_ R$'))
ctdr=0
while saque>=50:
    saque-=50
    ctdr+=1
print(f'{ctdr} notas de R$50.00.')
ctdr=0

while saque>=20:
    saque-=20
    ctdr+=1
print(f'{ctdr} notas de R$20.00.')
ctdr=0

while saque>=10:
    saque-=10
    ctdr+=1

print(f'{ctdr} notas de R$10,00.')
ctdr=0
while saque>=5:
    saque-=5
    ctdr+=1

print(f'{ctdr} notas de R$5,00')
ctdr=0

while saque>=1:
    saque-=1
    ctdr+=1

print(f'{ctdr} notas de R$1,00.')

