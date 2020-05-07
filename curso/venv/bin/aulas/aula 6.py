# tipos primitivos#
n1 = input('Digite um numero')
n2 = input('Digite mais um numero')
s=n1+n2
print('A soma vale', s)
#vai dar errado pois ira mostrar o resultado dos conjunto 3+2= 32#
n3 = int(input('Digite um Numero:'))
n4 = int(input('Digite outro Numero:'))
s2=  n3+n4
#significado do numero primitivo
#int = numero inteiro: 7;-4;0;9875
#float = numeros reais ou flutuantes: 4.5;0.076;-15.223; 7.0
#bool = valores logicos:True(colocar o T maiusculo); False(mesma coisa)
#str = valores caracteres:'olá','7.5';''(aspas vazia);####
#print('A soma entre',n3,'e',n4,'vale{}'.format(s2))
print('A soma entre {} e {} vale {}'.format(n3, n4, s2))
print(type(s2))
