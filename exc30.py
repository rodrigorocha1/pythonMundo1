'''
Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
'''
print("+´´-" * 20 , "Par ou ímpar", "+´´-" * 20)
num = int(input('Digite um número: '))
if num % 2 == 0:
    print(f'O número {num} é par')
else:
    print(f'O número {num} é ímpar')