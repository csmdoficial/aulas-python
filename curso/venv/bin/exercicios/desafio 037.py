"""escreva um programa que leia um numero inteiro qualquer e peça
para o usuario escolher qual será a base de conversão:
-1 para binario
-2 para octal
-3 para hexadecimal"""
num = int(input('Escreva um numero inteiro:'))
print('Escolha a base de conversão:')
print('''
[1]- Binário
[2]- Octal
[3]- Hexadecimal  ''')
resposta = int(input(''))

if resposta == 1:
    print('{} convertido para binario é igual à {}'.format(num,bin(num)[2:]))
elif resposta == 2:
    print('{} convertido para octal é igual à {}'.format(num,oct(num)[2:]))

elif resposta == 3:
    print('{} convertido para hexadecimal é igual à {}'.format(num,hex(num)[2:]))
else:
    print('Opção inválida, Tente novamente:')