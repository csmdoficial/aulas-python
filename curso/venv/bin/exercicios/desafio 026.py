"""faça um programa que leia uma frase pelo teclado e mostre
- quantas vezes aparece a letra a
-em que posição ela aparece
- em qu posição ela aparece a ultima vez
"""
frase = str(input('Digite uma frase:')).strip()
qtas = frase.upper().count('A')
posição = frase.upper().find('A')  +1
posição_final = frase.upper().rfind('A') +1
print('Na frase escrita temos {} letras A, na primeira posição {} e na ultima na {}'.format(qtas,posição, posição_final))
