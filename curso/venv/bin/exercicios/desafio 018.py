'''faça um programa que leia um angulo qualquer e mostre na tela o valor do seno,
cosseno e tangente desse angulo'''
import math
an = float(input('Digite o ângulo que você deseja:'))
seno = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('o seno é de {:.2f}'.format(seno))
print('O cosseno é de {:.2f}'.format(cos))
print('A tangente é de {:.2f}'.format(tan))