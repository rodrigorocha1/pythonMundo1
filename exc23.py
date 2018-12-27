'''Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.'''
print('*' * 20, 'Separar número', '*' * 20)
num = int(input('Digite um número: '))

unidade = num % 10  # Captura a unidade do número
dezena = (num % 100) // 10  # Captura a dezena do número
centena = (num % 1000) // 100  # Captura a centena do número
milhar = (num % 10000) // 1000  # Captura o milhar

print(f'{num} partido em {milhar},{centena},{dezena} e {unidade}')

