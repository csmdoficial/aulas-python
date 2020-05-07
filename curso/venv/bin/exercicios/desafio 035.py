"""Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem
ou nao formar um triangulo"""
print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
reta1 = int(input("Primeira reta:"))
reta2 = int(input("Segunda reta:"))
reta3 = int(input("Terceira reta:"))
#cada um desses segmentos tem que ser menor que a soma do comprimento dos outros dois
if reta1 < (reta2+reta3) and reta2 < (reta1+reta3) and reta3 < (reta1+reta2):
    print("Os 3 segmentos formam um triângulo!")
else:
    print("Os 3 segmentos não formam um triângulo!")
