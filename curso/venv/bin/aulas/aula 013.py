""""
AULA 012 - ESTRUTURA DE REPETIÇÃO
Laços de repetição (parte 1)
for c in range(1,10):
    passo
pega
for c in range(0,3)
    passo
    pula
passo
pega
for c in range(0,3)
    if money:
        pega
    passo
    pula
passo
pega
"""
#exemplos
for c in range(0,100):# vai printar oi 100 vezes e depois no final vai falar fim
    print("Oi")
print('FIM')
for d in range(1,7): #vai contar de 1 até 6 e no final vai falar fim
    print(d)
print("Fim")
for f in range (6,0,-1): #vai contar de 6 até 1 e no final vai falar fim
    print(f)
print('Fim')
for g in range (0,7,2): #vai contar de 0 até 6 pulando de dois em dois
    print(g)
print('Fim')
n = int(input("Digite um numero:"))
for h in range (0 , n+1): # vai contar de 0 até o numero falado
    print(h)
print("Fim")
i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
for i in range (i, f+1 , p): # vai contar do numero escolhido até o final pulando de passo em passo
    print(i)
print("Fim")
s = 0
for j in range (0,10):
    n = int(input("Digite um valor:"))
    s += n
print("O somatório de todos os valores foi {}".format(s))