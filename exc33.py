'''Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

listaDeNumeros = [n1, n2, n3]
listaDeNumeros.sort()
print(f'Menor Número: {listaDeNumeros[0]} \nMaior número: {listaDeNumeros[2]}')

