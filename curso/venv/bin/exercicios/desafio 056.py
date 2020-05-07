"""desenvolva um programa que leia o nome, idade, e sexo de 4 pessoas
no final do programa, mostre:
- a media de idade do grupo.
-qual é o nome do homem mais valeho
-quantas mulheres tem menos de 20 anos"""
somaidade = 0
maioridadehomem = 0
nomevelho =" "
for p in range(1,5):
    print("___________ {}ª PESSOA __________".format(p))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    somaidade += idade
    contm = 0

    if p == 1 and sexo in "Mm":#saber se o primeiro homem é o mais velho
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Mm" and idade > maioridadehomem:# caso nao seja o primeiro, saber qual é o mais velho
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:#quantas mulheres são menor de 20 anos
        contm += 1

print("A média de idade do grupo é de {} anos!".format(somaidade/4))
print("O homem mais velho tem {} anos e se chama {}".format(maioridadehomem ,nomevelho.capitalize()))
print("Ao todo são {} mulheres com menos de 20 anos".format(contm))

