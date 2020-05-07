"""condicoes aninhadas
if  carro.esquerda():
    carro.siga()
    carro.direita()
    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.direita()
    carro.siga()
elif(else+if) carro.direita():
    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.esquerda()
    carro.siga()
else:
    carro.siga
carro.pare()
"""
#pratica
nome = str(input('Qual é seu nome?')).upper()
if nome == 'VINICIUS':
    print('Que nome Bonito!')
elif nome == "ETHAN" or "ClAUDIO":
    print('Ual que nome massa!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia {}'.format(nome.capitalize()))