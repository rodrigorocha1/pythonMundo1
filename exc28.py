'''
Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

import time
import random

palpiteCPU = random.randint(0, 5)
palpiteJogador = int(input("Digite um número de 0 a 5: "))
print('Processando....')
time.sleep(2)
if palpiteCPU > palpiteJogador:
    print('O computador ganhor')
elif palpiteCPU < palpiteJogador:
    print('O jogador ganhou')
else:
    print('Empate')

