'''
Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
'''

nome = str(input('Digite o nome: ')).lower()
print(f'Seu nome tem Silva ?: {"silva" in nome.split()}')
