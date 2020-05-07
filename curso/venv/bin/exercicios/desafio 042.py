"""Refaça o desafio 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo
será formado
-equilatero: todos os lados iguais
isosceles: dois lados iguais
- Escaleno: todos os lados diferentes"""
r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1+ r3 and r3 < r1+r2:
    print('Os segmentos acima podem formar um triângulo!')
    if r1 == r2 == r3:
        print('Este é um triângulo EQUILÁTERO!!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Este é um triângulo ISÓCELES!!')
    else:
        print('Esté é um triângulo ESCALENO!!')
else:
    print('Os segmentos não podem formar um triângulo!')