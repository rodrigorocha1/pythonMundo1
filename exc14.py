'''Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.'''
tempCelsius = float(input('Digite a temperatura em celsius: '))
tempFahr = (tempCelsius * (9 / 5)) + 32

print(f'{tempCelsius}ºc equivale a {tempFahr}ºf')


