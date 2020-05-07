"""faça um programa qu leia três números e mostre qual é o menor e o maior """
a = float(input("Digite um numero:"))
b = float(input("Digite outro numero:"))
c = float(input('Digite o ultimo numero:'))
#verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {:.0f}'.format(menor))
print('O maior valor digitado foi {:.0f}'.format(maior))



