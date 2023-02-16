#programa para calcular se uma pessoa pode financiar uma casa
valor_casa=float(input('informe o valor a financiar_'))
tempo=int(input('informe o tempo em meses para quitar o financiamento_'))
sal=float(input('informe seu salário_'))
valor_tempo=valor_casa / tempo
parcela=sal*0.3

if valor_tempo > parcela:
    print('valor para finaciamento não aprovado')
else:
    print('vc pagará {:.2f} por mês, durante {} meses'.format(valor_tempo,tempo))
