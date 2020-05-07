"""crie um programa que leia dois valores e mostre um menu como o ao lado na tela:
seu programa deverá realizar a operação solicitada em cada caso
[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa """
from time import sleep
n1 = float(input("Primeiro valor: "))
n2 = float(input("Segundo valor: "))
resposta = 0
while resposta != 5:
    print("="*50)
    print("""
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do programa
    """)
    print("="*50)
    resposta = int(input("Qual é sua opção? "))
    if resposta == 1:
        print("A soma de {} + {} = {}".format(n1,n2, n1+n2))
    elif resposta ==2:
        print("A Multiplicação de {} * {} = {}".format(n1,n2, n1*n2))
    elif resposta == 3:
        if n1 > n2:
            print("O maior numero entre {} e {} é {}".format(n1,n2,n1))
        elif n2 > n1:
            print("O maior numero entre {} e {} é {}".format(n1,n2,n2))
    elif resposta == 4:
        n1 = float(input("Primeiro valor"))
        n2 = float(input("Segundo valor"))
    sleep(2)
print("Você saiu do programa!!")