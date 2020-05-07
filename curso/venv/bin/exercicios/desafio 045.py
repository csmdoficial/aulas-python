"""CRIE UM PROGRAMA QUE FAÇA O COMPUTADOR JOGAR JOKENPO COM VOCÊ"""
print("""
Sua opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA""")
from random import randint
itens = ('Pedra',"Papel","Tesoura")
pc = randint(0,2)
play = int(input("Qual é sua jogada? "))
print("================= Jogadas ================")
print("O computador escolheu {}".format(itens[pc]))
print("O jogador escolheu {}".format(itens[play]))
print('==========================================')
if pc == 0: #pedra
    if play == 0:
        print("Empatou!!")
    elif play == 1:
        print("O Jogador venceu!")
    elif play == 2:
        print("O Computador venceu!")
    else:
        print("Jogada Invalida!")
elif pc == 1: #papel
    if play == 0:
        print("O Computador Venceu!")
    elif play == 1:
        print("Empatou!")
    elif play == 2:
        print("O Jogador venceu")
    else:
        print("Jogada Invalida!")
elif pc == 2: #tesoura
    if play == 0:
        print("O Jogador venceu!")
    elif play == 1:
        print("O Computador venceu!")
    elif play == 2:
        print("Empatou!")
    else:
        print("Jogada Invalida!")