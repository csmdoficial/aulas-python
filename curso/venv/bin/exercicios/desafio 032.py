"""faça um programa que leia um ano qualquer e mostre se ele é bissexto"""
ano = int(input('Qual o ano?:'))
if (ano%4 ==0 and ano%100!=0) or (ano%400==0):
    print('Bissexto')
else: print('Não é bissexto')
#Anos bissextos são aqueles que são múltiplos de 4, como 1996, 2000, 2004 etc
# (que podem ser divididos por 4 deixando resto 0).
#Porém, há uma exceção: múltiplos de 100 que não sejam múltiplos de 400.
