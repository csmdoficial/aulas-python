"""Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
termos da progressçao usando a estrutura while"""
print("Gerador de PA")
print("-="*50)
primeirotermo = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
term = primeirotermo
cont = 1
while cont <=10 :
    print("{} -> ".format(primeirotermo), end="")
    primeirotermo = primeirotermo + razao
    cont += 1
print("FIM")

