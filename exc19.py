'''
Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
'''
import random
nome = []
for x in range(1, 5):
    nome.append(str(input(f'Digite {x}º nome de 4: ')))
print(f'Lista de nomes {nome}')
print(f'Nome escolhido: {random.choice(nome)}')
