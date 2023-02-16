# programa para calcular forma de pagamento de uma compra
print('{:^40}'.format('loja do guga'))
valor=float(input('digite o valor_'))
print('valor da compra é R${:.2f}'.format(valor))
f_pgto=int(input('''escolha a forma de pagamrnto
[1] a vista cheque/dinheiro 10% desconto
[2] a vista no cartão 5% desconto
[3] em 2x no cartão. preço anunciado
[4] 3x ou mais. 20% de juros_'''))

if f_pgto==1:
    conta=valor*0.9
    print('vc pagará R${:.2f}'.format(conta))

elif f_pgto==2:
    conta=valor*0.95
    print('vc pagará RS{:.2f}'.format(conta))
elif f_pgto==3:
    parcela=valor/2
    print('vc pagará 2x de R${:.2f}'.format(parcela))
elif f_pgto==4:
    conta=valor*1.2
    parcela=int(input('digite quantas parcelas_'))
    boleto=conta/parcela
    print('vc pagará {}x de R${:.2f}'.format(parcela,boleto))
else:
    print('forma de pagamento inválida. {:.2f} deve ser pago à vista'.format(valor))
    

print('f_pgto escolhida {}.'.format(f_pgto))

