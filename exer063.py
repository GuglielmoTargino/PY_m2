#programa para se calcular a sequencia de fibonacci
n=int(input('Digite quntos termos vc quer saber_'))
t0=0
t1=1
c=2
print('{} > {} > '.format(t0,t1), end='')
while c<n:
    t3=t0+t1
    print('{} > '.format(t3), end='')
    c+=1
    t0=t1
    t1=t3

print('FIM')

print('>'*30)
print('<'*30)
