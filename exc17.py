'''Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto
adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
'''

import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))

h = math.sqrt(math.pow(co,2) + math.pow(ca,2))

print(f'O valor da hipotenusa: {h:.2f}')
