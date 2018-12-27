'''
Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''
import math
ang = float(input('Digite o ângulo: '))
print(f'Seno de {ang:.2f} = {(math.sin(math.radians(ang))):.2f}')
print(f'Cosseno de {ang:.2f} = {math.cos(math.radians(ang)):.2f}')
print(f'Tangente de {ang:.2f} = {math.tan(math.radians(ang)):.2f}')


