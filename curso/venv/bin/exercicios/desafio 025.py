"""crie um programa que leia o nome de uma pessoa e diga se ela tem 'silva' no nome"""
nome = str(input('Digite um nome:')).upper().strip()
print('SILVA'in nome)
n = str(input('Digite um nume:')).upper().strip()
print('Seu nome tem Silva? {}'.format('SILVA' in n))
