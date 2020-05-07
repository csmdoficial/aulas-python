"""AULA 10 = CONDIÇÕES
- até agroa fazemos os exercicios em uma ordem so da esquerda pra direita e de cima pra baixo
agora vamos começar a programar com condições, os seja muitiplas variaveis \
ex: se carro.esquerda senão (faz o outro caminho)\
vamos usar a ordem de cima pra baixo
ex:
se carro,esquerda()\
    carro.siga()\
    carro.direita()\
    carro.siga()\
    carro.esquerda()
    carro.siga()
    carro.direita()
    carro.siga()
senão
    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.esquerda()
    carro.siga()
carro.pare()

se carro.esquerda()          if carro.esquerda():
    bloco_V_                        bloco True
senão                         else:
    bloco_f_                    bloco False

tempo = int(input('Quantos anos tem seu carro?'))
if tempo <=3:
    print('carro novo')
else
    print('carro velho')
print('__FIM__')

USANDO 3 LINHAS
tempo = int(input('Quantos anos tem seu carro?'))
print('carro novo' if tempo <=3 else 'carro velho')
print('__FIM__')
"""
nome = str(input('Qual é seu nome?')).upper()
if nome == 'VINICIUS':
    print('Que nome lindo você tem!')
else:
    print('Que nome estranho!')
print('Bom dia {}'.format(nome.capitalize()))
n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2)/2
print('A sua média foi {:.2f}'.format(m))
if m >=6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
    