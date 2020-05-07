'''crie um programa que leia o nome completo da pessoa e mostre
-o nome com todas as letras maiuscula
- o nome com todas as letras minusculas
- quantas letras ao todo(sem considerar o espaço)
-quantas letras tem o primeiro nome
len = conta o espaço
'''
nome = str(input('Qual o seu nome?')).strip()
print(nome.upper())
print(nome.lower())
print(len(nome)-nome.count(' '))

list = nome.split()

print(len(list [0]))

