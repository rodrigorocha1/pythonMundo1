'''Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%'''

print('**' * 20, 'Aumento de salário', '**' * 20)

salarioFuncionario = float(input('Digite o salário do funcionário: '))

if salarioFuncionario > 1250.00:
    novoSalario = salarioFuncionario + (salarioFuncionario * 0.10)
else:
    novoSalario = salarioFuncionario + (salarioFuncionario * 0.15)

print(f'O funcionário, com salário de R$ {salarioFuncionario:.2f}, receberá um aumento de R$ {novoSalario:.2f}')


