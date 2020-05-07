"""elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
preço normal e condição de pagamento:
- à vista dinheiro/cheque 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- em 3X ou mais no cartão: 20% de juros"""
print("=======Loja Luca=======")
preco = float(input('Preço das compras: R$'))
print("""
FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x no cartão""")
opcao = int(input('Qual a sua opção? '))
if opcao == 1:
    print('Sua compra de R${} vai custar R${} no final.'.format(preco,preco*0.90))
elif opcao == 2:
    print('Sua compra de R${} vai custar R${} no final á vista no cartão.'.format(preco,preco*0.95))
elif opcao == 3:
    print("""
    [1] 1X no cartão 
    [2] 2x no cartão """)
    pc = int(input("Qual a sua Opção?: "))
    if pc == 1:
        print('Sua compra de R${} vai custar R${} no final parcelado no cartão em {}'.format(preco,preco,pc))
    elif pc == 2:
        print("Sua compra de R${} vai custar R${} no final parcelado no cartão em {} vezes de R${}".format(preco,preco,pc,preco/pc))
    else:
        print('Escolha outra opção de pagamento!')
elif opcao == 4:
    pcs = int(input("Em quantas vezes deseja fazer as compras?: "))
    print('Sua compra de R${} vai custar R${} no final parcelado no cartão em {} vezes'.format(preco,preco*1.20,((preco*1.20)/pcs)))
else:
    print('Escolha uma opção dentro das disponiveis!')