'''
Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''

import random


n1 = (str(input('Digite os nomes para sorteio: ')))
n2 = (str(input('Digite os nomes para sorteio: ')))
n3 = (str(input('Digite os nomes para sorteio: ')))
n4 = (str(input('Digite os nomes para sorteio: ')))
listaDeAlunos = [n1, n2, n3, n4]
random.shuffle(listaDeAlunos)
print(f'Lista de alunos sorteados: {listaDeAlunos}' )


