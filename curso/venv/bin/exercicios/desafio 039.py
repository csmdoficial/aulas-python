"""faça um programa que leia o ano de nascimento de um jovem e informe
 de acordo com sua idade, se ele ainda vai se alistar ao serviço militar,
 se é a hora de se alistar ou se ja passou do tempo do alistamento.
 seu programa tambem devera mostrar o tempo que passou do prazo"""
nc = int(input('Qual a sua data de nascimento?:'))
ano = 2020
alistar = 18
idade = (ano - nc)
falta = (18 - idade)
passou = (idade - 18)
anoalis = ano + falta
trasanos = ano - passou
if (ano - nc) < alistar:
    print('''
    Você tem {} anos, ainda falta {} para se alistar.
    Seu alistamento vai ser em: {}'''.format(idade,falta,anoalis) )
elif (ano - nc) > alistar:
    print('''
    Você tem {} anos, já devia ter se alistado à {} atrás.
    Seu alistamento foi em: {}'''.format(idade,passou,trasanos ))
else:
    print('Você deve se alistar URGENTEMENTE!!!!')
