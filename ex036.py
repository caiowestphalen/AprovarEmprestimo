# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite quanto você recebe por mês: R$'))
anos = int(input('Digite em quantos anos pretende pagar: '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='' )
print(' a prestação será de R${:.2f}. Seu salário é de R${:.2f}'.format(prestacao, salario))
if prestacao <= minimo:
    print('PARABÉNS! Seu empréstimo foi aprovado!')
else:
    print('Seu empréstimo foi negado!')




