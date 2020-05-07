"""faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
eo ultimo nome separadamente"""
nome = str(input('Qual o seu nome?')).strip()
list = nome.split()
print('Primeiro nome: {}'.format(list[0]))

print('Ultimo nome: {}'.format(list[len(list)-1]))

