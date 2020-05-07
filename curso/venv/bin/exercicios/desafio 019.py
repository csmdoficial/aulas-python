''' O professor quer sorteador um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo
o nome e escrevendo o nome do escolhido'''
import random
a1 = input("Primeiro aluno:")
a2 = input('Segundo aluno:')
a3 = input('Terceiro aluno:')
a4 = input('Quarto aluno:')
lista = [a1,a2,a3,a4]
escolhido = random.choice(lista)
print("O aluno sorteado foi {}".format(escolhido))
