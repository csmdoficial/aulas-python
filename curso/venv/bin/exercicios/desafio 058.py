"""melhore o jogo do desafio 028 onde o computador vai "PENSA" EM UM NUMERO ENTRE 0 E 10
SO QUE AGORA O JOGAGOR VAI TENTAR ADIVINHAR ATÉ ACERTAR, MOSTRANDO NO FINAL QUANTOS PALPUTES
FORAM NECESSARIOS PARA VENCER"""
print("Olá sou seu computador...")
print("Estou pensando num número de 0 a 10")
print("Tente adivinhar:  ")
chute = int(input("Qual número estou pensando?: "))
import random
list = [0,1,2,3,4,5,6,7,8,9,10]
pc = random.choice(list)
print(pc)
t = 1
while chute != pc:
    t += 1
    if chute > pc:
        chute = int(input("Um pouco Menos: "))
    else:
        chute = int(input("Um pouco Mais: "))
print("Parabens você acertou com {} tentativas".format(t))
