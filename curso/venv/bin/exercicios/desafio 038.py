"""Escreva um programa que leia dois numeros inteiros e compare-os,
mostrando na tela uma mensagem:
- o primeiro valor é maior
- o segundo valor é maior
- não existe valor maior, os dois são iguais"""
n1 = float(input('Digite o primeiro numero:'))
n2 = float(input('Digite o segundo numero:'))
if n1 > n2:
    print('O primeiro valor é maior que o segundo!')
elif n2 == n1:
    print('Os valores são Iguais!')
else:
    print('O segundo valor é maior que o primeiro!')