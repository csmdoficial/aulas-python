"""escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.
o programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar
calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario ou
então o emprestimo será negado"""
valor = float(input('Qual o valor da casa?'))
salario = float(input('Qual o seu salario?'))
anos = int(input('Em quantos anos?'))
#a prestação tem que ser 30% pra baixo
meses = anos*12
conta = valor/meses
porcento= salario*0.30
if conta <= porcento:
    print("Parabens o seu emprestimo foi aceito.")
    print('O valor da sua parcela é de R${}'.format(conta))
else:
    print('Opa seu emprestimo não foi aceito, sinto muito')