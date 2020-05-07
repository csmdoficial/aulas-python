"""Desenvolva um programa que pergunte a distancia de uma viagem em km.
calcule o preço da passagem, cobrando R$ 0,50 por km para viagens até 200 km
e R$ 0,45 para viagen mais longas"""
distancia = float(input('Tamanho da Viagem em KM:'))
if distancia <= 200.00:
    print("O Valor da sua viagem foi de R${}".format(distancia*0.50))
else:
    print('O valor da sua viagem foi de R${}'.format(distancia*0.45))