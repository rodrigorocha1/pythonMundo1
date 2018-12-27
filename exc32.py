'''Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.'''

import datetime
from datetime import date
print("*" * 20, 'Ano bissesto', "*" * 20)
ano = int(input('Digite o ano <0 para atual> '))

if ano == 0:
    anoAtual = date.today().year
    if anoAtual % 100 != 0 and anoAtual % 4 == 0 or anoAtual % 400 == 0:
        print(f'{anoAtual} é bissesto')
    else:
        print(f'{anoAtual} não é bissesto')
else:
    if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
        print(f'{ano} é bissesto')
    else:
        print(f'{ano} não é bissesto')

