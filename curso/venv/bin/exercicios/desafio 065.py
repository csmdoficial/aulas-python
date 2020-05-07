"""crie um programa que leia varios numeros inteiros pelo teclado, no final
da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
o programa deve perguntar ao usuario se ele quer ou nao continuar a digital valores"""
r = "S"
soma = maior = menor = c = media = 0

while r in "Ss":
    n = int(input("Digite um número: "))
    soma += n
    c += 1
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
           maior = n
        if n < menor:
            menor = n

    r = str(input("Você quer continuar? [S/N]: ")).strip().upper()[0]
media = soma / c
print("Você digitou {} números, a média entre eles foi {}".format(c , media))
print("O maior valor foi {} e o menor foi {}".format(maior,menor))
