"""" LAÇOS DE REPETIÇÃO (2)
    -ESTRUTURA DE REPETIÇÃO WHILE
    Quando não sabemos quantas repetições teremos que fazer, não podemos usar mais o for
    e então precisaremos usar outra estrutura de repetição. Chamamos então de estrutura de
    repetição com teste logico.
    enquanto não chegar na maça
        passo
    pega
    em comando python
    while not maça:
        passo
    pega

    Outro exemplo
    enquanto não maça:
        se tiver chão:
            passo
        se tiver buraco:
            pule
        se tiver moeda:
            pegue
    pega
    Em comando python
    while não maça:
        if tiver chão:
            passo
        if tiver buraco:
            pule
        if tiver moeda:
            pegue
    pega
"""
# na pratica
"""for d in range(1,10):
    print (d)
print('Fim')"""
"""c =1
while c <10:
    print(c)
    c+=1
print("fim")

n = 1
while n != 0:
    n = int(input("Digite um valor: "))
print("Fim")

resposta = "Sim"
while resposta == "SIM" or resposta == "S":
    n = int(input("Digite um valor: "))
    resposta = str(input("Quer continuar? [Sim/Não]")).upper()

print("Fim")"""

n = 1
par = impar = 0
while n != 0:
    n = int(input("Digite um valor:"))
    if n != 0:
        if n % 2 ==0:
            par += 1
        else:
            impar += 1
print("você digitou {} numeros pares e {} numeros ímpares".format(par,impar))

