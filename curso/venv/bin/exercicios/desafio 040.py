"""crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
-média abaixo de 5.0: recuperação
-média entre 5.0 e 6.9: recuperação
- média 7.0 ou superior : aprovado"""

p1 = float(input('Nota da primeira prova:'))
p2 = float(input('Nota da segunda prova:'))
media = (p1+p2)/2
print('Sua média foi de {:.2f}'.format(media))
if media < 5.0:
    print('Você está reprovado!')
elif media >= 7.0:
    print('Você está aprovado!')
else:
    print('Você está de recuperação!')
