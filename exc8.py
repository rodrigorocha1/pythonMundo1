'''
Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido
 em centímetros e milímetros.
'''

metros = float(input("Digite o valor para ser convertidos em centímetros e mílimetros: "))
print(f'{metros:.2f} equivale a {100 * metros:.2f} metros e {1000 * metros:.2f} milimetros')
