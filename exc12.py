'''
Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
'''

precoDoProduto = float(input('Digite o valor do produto '))
valorComDesconto = precoDoProduto - (precoDoProduto * 0.05)
print(f'O produto de valor R${precoDoProduto:.2f} reais, com 5% de desconto, será no valor de R$ {valorComDesconto:.2f}')