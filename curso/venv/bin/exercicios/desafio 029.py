"""escreva um programa que leia a velocidade de um carro
se ele ultrapassar 80km, mostre uma mensagem dizendo que ele foi multado
a multa vai custar R$7,00 para cada km acima do limite"""
velocidade = float(input('Velocidade do carro:'))
soma_multa = (velocidade - 80)*7
if velocidade > 80:
    print("Atenção, você foi multado em R${:.2f}, devido a alta velocidade em um local".format(soma_multa))
