'''
Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
3.90
'''

dinheiroNaCarteira = float(input('Digite o valor total do dinheiro na carteira: '))

print(f'Com R$ {dinheiroNaCarteira} reais, você pode comprar {dinheiroNaCarteira * 3.90:.2f}')
