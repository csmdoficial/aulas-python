"""Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas
daqueles que forem pares, se o valor digitado for impár. descondsidere-o"""
soma = 0
cont = 0
for c in range(1,7):
    n = int(input("Digite o {} numero: ".format(c)))
    if n %2 ==0 :
        soma = soma + n
        cont = cont + 1
print("Você informou {} números e a soma foi {}".format(cont, soma))