'''
Exercício Python 029: Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
'''

velocCarro = float(input('Digite a velocidade do carro: '))

if velocCarro <= 80:
    print('Tenha um bom dia')
else:
    print(f'Você foi multado em R$ {(velocCarro - 80) * 7.00:.2f}')
    print()

