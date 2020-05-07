"""crie um programa que leia uma frase qualquer e diga se ela é um palindromo,
desconsiderando os espaços"""
frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = '' . join(palavras)
print("Você digitou a frase {}".format(junto))
inverso = ""
for letra in range(len(junto)-1, -1 , -1):
    inverso += junto[letra]
print("A palavra {} lida de trás pra frente fica {}".format(junto,inverso))
if junto == inverso:
    print("Está frase é um palindromo!")
else:
    print("Está frase não é um palindromo!")