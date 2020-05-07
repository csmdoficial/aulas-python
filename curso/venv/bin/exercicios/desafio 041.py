"""A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um
atleta e mostre sua categoria, de acordo com a idade:
-até 9 anos:MIRIM
até 14 anos infantil
até 19 anos junior
até 25 anos senior
acima: master"""
from datetime import date
nc = int(input('Qual o ano de nascimento?:'))
atual = date.today().year
idade = int(atual - nc)
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print("Ele irá participar da categoria MIRIM!")
elif idade <=14:
    print('Ele irá participar da categoria Infantil!')
elif idade <=19:
    print('Ele irá participar da categoria JUNIOR!')
elif idade <= 25:
    print('Ele irá participar da categoria SÊNIOR!')
else:
    print('Ele irá participar da categoria MASTER!')