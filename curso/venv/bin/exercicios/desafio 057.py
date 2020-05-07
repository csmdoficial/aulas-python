"""faça um programa que leia o sexo de uma pessoa, mas so aceite os valores
"M" ou "F". caso esteja errado, peça a digitação novamente até ter um valor correto"""
nome = str(input("Qual o nome da pessoa: ")).strip().upper()[0]
sexo = str(input("Qual o sexo dessa pessoa? [F/M]: ")).strip().upper()[0]
while sexo not in "MmF":
    sexo = str(input("Dados invalidos, Por Favor Informe seu Sexo: ")).strip().upper()[0]
print("Sexo {} registrado com sucesso".format(sexo))