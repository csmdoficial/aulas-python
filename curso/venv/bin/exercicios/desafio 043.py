"""desenvolva um logica que leia o peso e a altura de uma pessoa,
calcule seu imac e mostre seu status, de acordo com a tabela abaixo:
-abaixo de 18.5: Abaixo do Peso
-entre 18.5 e 25: peso ideal
-25 até 30: sobrepeso
-30 até 40: obesidade
-acima de 40: obesidade morbida
"""
peso = float(input("Qual é seu peso?(KG):"))
altura = float(input("Qual é sua altura?(m):"))
imc = peso/(altura*altura)
print('Olá, Você está com:')
if imc < 18.5:
    print("ABAIXO DO PESO")
elif imc < 25:
    print('PESO IDEAL')
elif imc < 30:
    print('SOBREPESO')
elif imc < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')