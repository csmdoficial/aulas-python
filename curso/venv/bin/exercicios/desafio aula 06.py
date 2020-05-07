n1 = int(input("Escolha um numero de 0 à 10"))
n2 = float(input('Escolha um numero fatorado de 0 à 1'))
s = n1+n2
print('A soma entre {} e {} da o resultado de {}'.format(n1,n2,s))
## desafio 2
n = input('Digite algo')
print('esse texto representa',type(n))
print('Ele é uma letra?',n.isalpha())
print('Ele é um numero?', n.isnumeric())
print('Apresenta somente letra maiuscula?', n.isupper())
print('Apresenta somente letra minuscula?',n.islower())