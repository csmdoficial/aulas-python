""" Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento
 Para salarios superiores a 1250, calcule um aumento de10%
 para inferiores o iguais, o aumento é de 15%"""
salario = float(input("Salario de um funcionario:"))
if salario <= 1250:
    print("O salario passará para R${:.2f}".format((salario*(1.15))))
else:
    print("O salario passará para R${:.2f}".format((salario*(1.10))))