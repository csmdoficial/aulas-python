"""Crie um programa que leia varios numeros inteiros pelo teclado.
o programa só vai parar quando o usuario digitar o valor 999, que é a condição de parada
no final, mostre quanstos numeros foram digitados e qual foi a soma entre eles (desconsiderando o flag)"""
s = c = n = 0
n = int(input("Digite um Número [Para parar digite 999]: "))
while n != 999:
    c += 1
    s += n
    n = int(input("Digite um Número [Para parar digite 999]: "))
print("Você digitou {} números, a soma foi de {} ".format(c,s))
