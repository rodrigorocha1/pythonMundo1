'''
Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
'''

salFunci = float(input('Digite o valor do salário: '))
salFunciReaj = salFunci + (salFunci * 0.15)
print(f'O salário no valor de R${salFunci:.2f}, com 15% de aumento, será no valor de R$ {salFunciReaj:.2f} ')
