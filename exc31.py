'''Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
'''

distancia = float(input('Digite a distância em KM: '))
if distancia <= 200:
    precoDaPassagem = 0.50 * distancia
else:
    precoDaPassagem = 0.45 * distancia
print(f'Preço da passagem para {distancia} km = R${precoDaPassagem:.2f} ')


