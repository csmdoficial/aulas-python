dias = int(input("Quantos dias alugados?"))
km = float(input("Quantos km rodados?"))
valor = (dias * 60) + (km * 0.15)
print("O valor do aluguel foi de R${:.2f}".format(valor))
