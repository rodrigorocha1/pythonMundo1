'''Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um
carro alugado e a quantidade de dias pelos quais ele foi alugado.
 Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
 '''

kmPerco = float(input('Digite o total de km rodados: '))
qtdDias = int(input('Digite o total de dias alugados: '))

precoAPagar = (qtdDias * 60) + (kmPerco * 0.15)
print(f'Valor total: R$ {precoAPagar:.2f} reais')

