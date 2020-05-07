"""Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome'santo'"""
nome = str(input('Nome de uma cidade:')).strip()
separado = nome.upper().split()
print( 'SANTO' in separado [0])
cid = str(input('nome de uma cidade:')).strip()
print(cid[:5].upper() == 'SANTO')