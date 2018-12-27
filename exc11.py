'''
Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
'''

larguraDaParede = float(input('Digite a largura da parede em metros: '))
alturaDaParede = float(input('Digite a altura da parede em metros: '))

print(f'Sua parede tem dimensão de {larguraDaParede:.2} x {alturaDaParede:.3} e sua área é de {larguraDaParede * alturaDaParede:.4} m²')
print(f'Para pintar essa parede, será necessário {(larguraDaParede * alturaDaParede) / 2:.5} litros de tinta')

