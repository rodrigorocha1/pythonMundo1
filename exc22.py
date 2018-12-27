'''
Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.
'''

nome = (input('Digite o nome completo: ')).strip()

print(f'Nome em maiúsculo: {nome.upper()}')
print(f'Nome em minúsculo: {nome.lower()}')
totalDeLetras = len(nome)- nome.count(' ')
print(f'Total de letras: {totalDeLetras} letras')
primeiroNome = nome.find(' ')
print(f'Total de letras no primeiro nome: {primeiroNome}')


