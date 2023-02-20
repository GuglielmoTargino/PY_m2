#programa psrs se calcular ums PA variavel
ini=int(input('Digite o primwiro termo da PA_'))
raz=int(input('Digite a razão de PA_'))
termos=int(input('Digite quantos termos você quer saber?_'))
contador=0
mais=1

while mais!=0:
   

    while contador<termos: 
        
        print('PA é {}'.format(ini))
        ini+=raz
        contador+=1
    mais=int(input('Mais algum termo?_Quantos?'))  # linha para se fazer a pergunta quntos termos a mais
    termos+=mais    # linha para aumentar o limite do contador

print('Final com {} termos'.format(termos))



