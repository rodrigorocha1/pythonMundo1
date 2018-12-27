'''Exercício Python 035: Desenvolva um programa que leia o
comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.'''

l1 = float(input('Digite o comprimento da reta em cm: '))
l2 = float(input('Digite o comprimento da reta em cm: '))
l3 = float(input('Digite o comprimento da reta em cm: '))

if l1 <= l2 + l3 and l2 <= l1 + l3 and l3 <= l1 + l2:
    print(f'Os lados {l1}, {l2} e {l3} podem formar um triângulo: ')
else:
    print(f'Os lados {l1}, {l2} e {l3} não podem formar um triângulo ')


