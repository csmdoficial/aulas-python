#Operações Aritméticas
# + adição
# - Subtração
# * Multiplicação
# / Divisão
# ** Potência
# // Divisão Inteira
# % Resto da Divisão
# o Operador precisa de operandos, ex 5+; 5-; 5*.
# pode ser um numero uma string ou variaveis.
# os oepradores funcionam com binarios, ou seja ele precisa de dois operandos
# ex: 5+2; 5*2; 5/2;
#Utilizamos == dois iguais para quando eu quiser mostrar que uma coisa é igual a outra
#ORDEM
# 1- ()
# 2- **
# 3- *;/;//;%
# 4- +;-
###########################PRATICA###############################################
#poW função interna de potencia, mas perde preferencia
nome = input('qual é seu nome?')
print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Um valor:'))
n2 = int(input('Outro valor;'))
s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
e=n1**n2
print('soma{};\n multiplicação {};\ndivisão {};\ndivisão inteira {};\nexponencial {}'.format(s,m,d,di,e),end='>>>1')


