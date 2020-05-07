"""print("Gerador de PA")
print("-="*50)
primeirotermo = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
term = primeirotermo
cont = 1
while cont <=10 :
    print("{} -> ".format(primeirotermo), end="")
    primeirotermo = primeirotermo + razao
    cont += 1
print("FIM")"""
print("Gerador de PA")
print("-="*50)
termo = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print("{} -> ".format(termo), end = "")
        termo = termo + razao
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print("Progressão realizada com {} termos mostrados".format(total))
