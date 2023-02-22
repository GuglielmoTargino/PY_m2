
# exercicio para se calcular a media e qual foi o maior 
#numero digitado de uma sequencia.

fg='s'
menor=maior=0
ctor=soma=media=0

while fg!='N':
    nr=int(input('Digite um número_'))
    fg=str(input('Deseja continuar?_ [S/N]_')).upper().strip()[0]
    if ctor==0:
        menor=nr
    if nr>maior:
        maior=nr
    if nr<menor:
        menor=nr
    ctor+=1
    soma+=nr
    media=soma/ctor

print('Soma={}, Média={:.2f}, o maior foi={}, o menor foi ={}'.format(soma,media,maior,menor))


