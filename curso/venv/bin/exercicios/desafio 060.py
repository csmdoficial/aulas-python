from math import factorial
n = int(input("Digite um número:"))
f = factorial(n)
print("O fatorial de {} é {}".format(n,f))
#fazendo matematicamente
n = int(input("Digite um número: "))
c = n
f = 1
print("Calculando  {}! = ".format(n), end=" ")
while c > 0:
    print("{} ".format(c), end ="")
    print(' x ' if c > 1 else " = ", end = " ")
    f = f * c
    c-= 1
print("{}".format(f))