"""Refaça o Desafio 009, mostrando a tabuada de um numero que o usuario escolher,
so que agora utilizando um laço for"""
n = int(input("Digite um numero: "))
for c in range(1,11):
    print("{} x {:2} = {}".format(n, c , n*c))
